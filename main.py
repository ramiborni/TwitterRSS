import datetime
import json
import os
import random
import subprocess
from os import chdir
from pathlib import Path
import pytz
from feedgen.feed import FeedGenerator
import tomllib
from nltk.tokenize import word_tokenize
from twitter.scraper import Scraper
from twitter_data import twitter_data_from_dict

TWINT_API_DIR = Path(__file__).parent

# read configuration
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

list_categories = config["scrapper_config"]["categories"]

twitter_accounts = config['scrapper_config']['twitter_accounts']
within_time = config['scrapper_config']['within_time']
show_items = (config['scrapper_config']['show_items'])
if show_items == {} or show_items == 0:
    show_items = None

number_acc = [0] * len(list_categories)

feed_generators = []  # Array to hold the FeedGenerator instances

for category in list_categories:
    fg = FeedGenerator()
    fg.load_extension("media", rss=True, atom=True)
    fg.id(f'https://www.infokanal.com/{category["category_name"]}_rss.xml')
    fg.title(f'infokanal {category["category_name"]} RSS feed')
    fg.link(href=f'https://www.infokanal.com/{category["category_name"]}_rss.xml')
    fg.description('infokanal RSS feed for ' + category['category_name'])
    feed_generators.append(fg)


def is_date_in_range(date_str):
    if show_items is not None:
        return True
    date_format = "%a %b %d %H:%M:%S %z %Y"
    date = datetime.datetime.strptime(date_str, date_format)

    range_value, range_unit = int(within_time[:-1]), within_time[-1]

    if range_unit == "h":
        time_delta = datetime.timedelta(hours=range_value)
    elif range_unit == "d":
        time_delta = datetime.timedelta(days=range_value)
    elif range_unit == "m":
        # Assuming 30 days in a month
        time_delta = datetime.timedelta(days=range_value * 30)
    else:
        raise ValueError("Invalid date range format")

    # Assign the timezone of 'date' to 'now'
    now = datetime.datetime.now(date.tzinfo)

    return now - time_delta <= date <= now


def check_date_is_day(date) -> bool:
    start_time = datetime.time(hour=6)
    end_time = datetime.time(hour=18)
    return start_time <= date.time() <= end_time


def retrieve_random_image(username: str, date) -> str:
    day_or_night = "day" if check_date_is_day(date) else "night"
    USER_PATH = f'./Images/{username}/{day_or_night}'
    filenames = [f for f in os.listdir(
        USER_PATH) if os.path.isfile(USER_PATH + '/' + f)]
    if len(filenames) > 0:
        return f"http://www.infokanal.com/images/{username}/{day_or_night}/{random.choice(filenames)}"
    else:
        return ""


def filter_results(tweet_text, keywords) -> bool:
    for word in word_tokenize(tweet_text):
        for keyword in keywords:
            if keyword == word or keyword.lower() == word or keyword.replace(' ',
                                                                             '') == word or keyword.lower() == word.replace(
                    "#", "").lower():
                return True


def convert_to_RSS(item, keywords, fg, acc_type):
    global number_acc

    tweet = item['tweets']

    if filter_results(tweet['full_text'].replace("\n", " "), keywords) and is_date_in_range(tweet['created_at']):
        dt = datetime.datetime.strptime(
            tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
        new_dt = dt + datetime.timedelta(hours=2)

        prefix_time = new_dt.strftime("%H:%M")
        fe = fg.add_entry()
        fe.id(tweet['id'])
        fe.title(
            f"{item['prefix']} ({prefix_time}): {tweet['full_text']} {item['suffix']}")
        fe.link(href="https://twitter.com/twitter/status/" +
                     tweet['id'], rel='alternate')
        # parse datetime string and localize to UTC
        fe.pubDate(new_dt)

        if tweet['attachment']:
            fe.media.thumbnail({'url': tweet['attachment'], 'width': '200'},
                               group=None)
            fe.media.content({'url': tweet['attachment'], 'width': '400'},
                             group=None)
        else:
            result = retrieve_random_image(item['username'], dt)
            if result:
                fe.media.thumbnail(
                    {'url': result, 'width': '200'}, group=None)
                fe.media.content(
                    {'url': result, 'width': '400'}, group=None)

        acc_type_index = next(
                (index for index, category in enumerate(list_categories) if category["category_name"] == acc_type),
                None)
        number_acc[acc_type_index] = number_acc[acc_type_index] + 1
    else:
        return


def get_rest_ids(data):
    rest_ids = []
    for result_list in data:
        for result in result_list:
            rest_id = result['data']['user']['result']['rest_id']
            username = result['data']['user']['result']['legacy']['screen_name']
            rest_ids.append({
                "rest_id": rest_id,
                "username": username
            })
    return rest_ids


def get_max_res(binding_values):
    max_resolution = 0
    max_res_image_url = ""

    # Iterate through the BindingValue objects
    for binding_value in binding_values:
        image_value = binding_value.value.image_value

        # Check if the current BindingValue has an image_value
        if image_value:
            # Calculate the resolution (height * width) of the current image
            resolution = image_value.height * image_value.width

            # Update the maximum resolution and image URL if the current resolution is higher
            if resolution > max_resolution:
                max_resolution = resolution
                max_res_image_url = image_value.url

    return max_res_image_url


def print_tweets(res, users):
    list_tweets = []
    for item in res.data.user.result.timeline_v2.timeline.instructions:
        if item.entries is not None:
            for entry in item.entries:
                if entry.content.item_content is not None and entry.content.item_content.tweet_results.result.legacy is not None:
                    try:
                        user = list(filter(
                            lambda x: x[
                                          'rest_id'] == entry.content.item_content.tweet_results.result.legacy.user_id_str,
                            users))
                        max_res = ""
                        list_tweets.append({
                            'username': user[0]['username'],
                            'created_at': entry.content.item_content.tweet_results.result.legacy.created_at,
                            'full_text': entry.content.item_content.tweet_results.result.legacy.full_text,
                            'id': entry.content.item_content.tweet_results.result.legacy.id_str,
                            'attachment': max_res
                        })
                    except:
                        pass
    return list_tweets


def get_data():
    email, username, password = "ramyborni", "rikiraspoutine@gmail.com", "Raspoutine@5353"

    scraper = Scraper(email, username, password, debug=1, save=False)
    users = scraper.users([user['username'] for user in twitter_accounts])

    users_id = get_rest_ids(users)

    tweets = scraper.tweets([user['rest_id'] for user in users_id], limit=1000)

    result = []
    for tweet_data in twitter_data_from_dict(tweets):
        for tweets in tweet_data:
            result.append(print_tweets(tweets, users_id))

    return result


def get_date(item):
    return datetime.datetime.strptime(item['created_at'], '%a %b %d %H:%M:%S %z %Y')


def find_account_by_username(username):
    for account in twitter_accounts:
        if account['username'] == username:
            return account


if __name__ == '__main__':
    result = get_data()
    flat_result = [item for sublist in result for item in sublist]
    flat_result.sort(key=get_date, reverse=True)
    twitter_account_data = []
    for i in range(len(flat_result)):
        twitter_account_data = find_account_by_username(flat_result[i]['username'])
        if show_items is not None and all(item == show_items for item in number_acc):
            break

        for index in range(len(list_categories)):
            if number_acc[index] != show_items:
                category = list_categories[index]
                convert_to_RSS({
                    "username": flat_result[i]['username'],
                    "tweets": flat_result[i],
                    "prefix": twitter_account_data['prefix'],
                    "suffix": twitter_account_data['suffix']
                }, category['keywords'], feed_generators[index], category['category_name'])
                feed_list = feed_generators[index].entry()
                feed_generators[index].entry(sorted(feed_list, key=lambda x: x.pubDate(), reverse=True), replace=True)
                feed_generators[index].rss_str(pretty=True)
                feed_generators[index].rss_file(f'./rss/{category["category_name"]}_rss.xml')



