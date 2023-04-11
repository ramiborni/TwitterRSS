import datetime
import json
import os
import random
import subprocess
from os import chdir
from pathlib import Path
import pandas as pd
import pytz
from feedgen.feed import FeedGenerator
import tomllib

TWINT_API_DIR = Path(__file__).parent

# read configuration
with open("config.toml", "rb") as f:
    config = tomllib.load(f)
keywords = ' OR '.join(config['scrapper_config']['keywords'])
twitter_accounts = config['scrapper_config']['twitter_accounts']
within_time = config['scrapper_config']['within_time']

# config RSS
fg = FeedGenerator()
fg.load_extension("media", rss=True, atom=True)
fg.id('http://infokanal.com/feed')
fg.title('infokanal RSS feed')
fg.link(href='http://infokanal.com/')
fg.description('infokanal RSS feed')


def return_query_results(
        query: str
) -> subprocess:
    global TWINT_API_DIR
    chdir(TWINT_API_DIR)
    cmd = [
        'go',
        'run',
        'main.go',
        '-Query',
        query,
        '-Instance',
        'birdsite.xanny.family',
        '-Format',
        'json',
    ]
    # If Instance needs to be modified use a value from https://github.com/zedeus/nitter/wiki/Instances

    process = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    return process.stdout


def parse_json_returned(json_str: str) -> json:
    return json.loads(
        json.JSONEncoder().encode(
            json_str
        )
    )


def check_date_is_day(date) -> bool:
    start_time = datetime.time(hour=6)
    end_time = datetime.time(hour=18)
    return start_time <= date.time() <= end_time


def retrieve_random_image(username: str, date) -> str:
    day_or_night = "day" if check_date_is_day(date) else "night"
    USER_PATH = f'./Images/{username}/{day_or_night}'
    filenames = [f for f in os.listdir(USER_PATH) if os.path.isfile(USER_PATH + '/' + f)]
    if len(filenames) > 0:
        return f"http://www.infokanal.com/images/{username}/{day_or_night}/{random.choice(filenames)}"
    else:
        return ""


def convert_to_RSS(item):
    if (len(item['tweets']) > 0):
        for i in range(len(item['tweets']['id'])):
            index = str(i)
            fe = fg.add_entry()
            fe.id(str(item['tweets']['id'][index]))
            fe.title(f"{item['prefix']}{item['tweets']['text'][index]}{item['suffix']}")
            fe.link(href=item['tweets']['url'][index], rel='alternate')
            # parse datetime string and localize to UTC
            dt = datetime.datetime.strptime(item['tweets']['timestamp'][index], '%b %d, %Y · %I:%M %p %Z')
            dt = pytz.utc.localize(dt)
            fe.pubDate(dt)
            if len(item['tweets']['attachments'][index]) > 0:
                fe.media.thumbnail({'url': item['tweets']['attachments'][index][0]['url'], 'width': '200'})
                fe.media.content({'url': item['tweets']['attachments'][index][0]['url'], 'width': '200'})
            else:
                result = retrieve_random_image(item['username'], dt)
                if result:
                    fe.media.thumbnail({'url': result, 'width': '200'})
                    fe.media.content({'url': result, 'width': '200'})

    else:
        return


if __name__ == '__main__':
    for twitter_account in twitter_accounts:
        query_str = f"{keywords} from:{twitter_account['username']} within_time:{within_time}"
        json_str = return_query_results(
            query_str,
        )
        response_json = parse_json_returned(
            json_str
        )
        df = pd.read_json(
            response_json,
            lines=True
        )
        formatted_json = json.loads(df.to_json())
        # print(formatted_json)
        convert_to_RSS({
            "username": twitter_account['username'],
            "tweets": formatted_json,
            "prefix": twitter_account['prefix'],
            "suffix": twitter_account['suffix']
        })

fg.atom_str(pretty=True)
fg.rss_str(pretty=True)
fg.rss_file('rss.xml')
fg.atom_file('atom.xml')
