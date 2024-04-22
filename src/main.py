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
from dotenv import load_dotenv
import os
from functions import save_filtered_data, check_tweet_exist, get_tweets_db
from police_fetch import get_police_news
from helpers import check_date_is_day, retrieve_random_image

load_dotenv()

import nltk

nltk.download('punkt')

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
    fg.lastBuildDate(datetime.datetime.now(tz=pytz.timezone('Europe/Oslo')))
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


def filter_results(tweet_text: str, keywords) -> bool:
    for word in word_tokenize(tweet_text):
        for keyword in keywords:
            if keyword == word or keyword.lower() == word or keyword.replace(' ',
                                                                             '') == word or keyword.lower() == word.replace(
                "#", "").lower() or (" " in keyword and keyword.lower() in tweet_text.lower()):
                return True


def save_db(item):
    tweet = item['tweets']
    if check_tweet_exist(tweet['id']):
        return

    # Assuming tweet['created_at'] is a string containing the tweet's creation date
    # and time in UTC.
    tweet_time = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')

    # Convert the datetime object to the desired timezone (Europe/Oslo)
    oslo_timezone = pytz.timezone('Europe/Oslo')
    tweet_time_oslo = tweet_time.replace(tzinfo=pytz.utc).astimezone(oslo_timezone)
    tweet_time_timestamp = tweet_time_oslo.timestamp()

    # Format the time in Europe/Oslo timezone
    prefix_time_oslo = tweet_time_oslo.strftime("%H:%M")

    # Construct the tweet body
    tweet_body = f"{item['prefix']} ({prefix_time_oslo}): {tweet['full_text']} {item['suffix']}"

    tweet_link = "https://twitter.com/twitter/status/" + tweet['id']

    thumbnail = ""
    if tweet['attachment']:
        thumbnail = tweet['attachment']
    else:
        thumbnail = retrieve_random_image(item['username'], tweet_time_oslo)

    if "replies" in tweet and tweet["replies"] is not None and tweet["replies"]:
        for tweet_reply in tweet["replies"]:
            tweet_reply[
                "tweet_body_rss"] = f"{item['prefix']} ({prefix_time_oslo}): {tweet_reply['full_text']} {item['suffix']}"

        data = {
            "username": item['username'],
            "id": tweet['id'],
            "tweet_body": tweet['full_text'],
            "tweet_body_rss": tweet_body,
            "thumbnail": thumbnail,
            "pub_date": tweet_time_timestamp,
            "link": tweet_link,
            "replies": tweet["replies"] or None,
            "is_police": False
        }
    else:
        data = {
            "username": item['username'],
            "id": tweet['id'],
            "tweet_body": tweet['full_text'],
            "tweet_body_rss": tweet_body,
            "thumbnail": thumbnail,
            "pub_date": tweet_time_timestamp,
            "link": tweet_link,
            "replies": None,
            "is_police": False
        }
    save_filtered_data(data)


def convert_to_RSS(item, keywords, negative_keywords, fg, acc_type, no_filter: bool):
    global number_acc

    if no_filter is True or (filter_results(item['tweet_body'].replace("\n", " "), keywords) and is_date_in_range(
            item['pub_date']) and not filter_results(item['tweet_body'].replace("\n", " "), negative_keywords)):

        fe = fg.add_entry()
        fe.id(item['id'])
        fe.title(item['tweet_body_rss'])
        fe.link(href=item['link'], rel='alternate')

        # Assuming pub_date is a Unix timestamp representing the publication date in Oslo timezone
        pub_date_timestamp = item['pub_date']  # Assuming this is a Unix timestamp

        # Convert the timestamp to a datetime object in UTC
        pub_date_utc = datetime.datetime.fromtimestamp(pub_date_timestamp, tz=pytz.utc)

        # Convert the UTC datetime to Oslo timezone
        oslo_timezone = pytz.timezone('Europe/Oslo')
        pub_date_oslo = pub_date_utc.replace(tzinfo=pytz.utc).astimezone(oslo_timezone)

        # Now, set the publication date in your feed generator
        fe.pubDate(pub_date_oslo)

        fe.media.thumbnail({'url': item['thumbnail'], 'width': '200'},
                           group=None)
        fe.media.content({'url': item['thumbnail'], 'width': '400'},
                         group=None)

        acc_type_index = next(
            (index for index, category in enumerate(list_categories) if category["category_name"] == acc_type),
            None)
        number_acc[acc_type_index] = number_acc[acc_type_index] + 1

        if "replies" in item and item["replies"] is not None and item["replies"]:
            for reply in item['replies']:
                print("IM REPLY")
                fe = fg.add_entry()
                fe.id(reply['id'])
                fe.title(reply['tweet_body_rss'])
                fe.link(href=item['link'], rel='alternate')
                datetime_reply = datetime.datetime.strptime(reply['created_at'], '%a %b %d %H:%M:%S %z %Y')
                pub_date_reply = datetime_reply
                print(pub_date_reply)
                print(reply['tweet_body_rss'])
                print("----------------------------------------------------------------")
                fe.pubDate(pub_date_reply)
                fe.media.thumbnail({'url': item['thumbnail'], 'width': '200'},
                                   group=None)
                fe.media.content({'url': item['thumbnail'], 'width': '400'},
                                 group=None)
                number_acc[acc_type_index] = number_acc[acc_type_index] + 1

    else:
        return


def get_rest_ids(data):
    rest_ids = []
    for result in data:
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


def tweet_type(entry, users):
    tweet_entry_id = entry["entryId"]
    if "tweet-" in tweet_entry_id:
        return extract_normal_tweet(entry, users)
    if "profile-conversation-" in tweet_entry_id:
        return extract_tweet_replies(entry, users)
    else:
        pass


def print_tweets(res, users):
    list_tweets = []

    try:
        instructions = res['data']['user']['result']['timeline_v2']['timeline']['instructions']

        for item in instructions:
            if 'entries' in item and item['type'] == "TimelineAddEntries":
                entries = item['entries']
                for entry in entries:
                    list_tweets.append(tweet_type(entry, users))
    except Exception as e:
        pass

    return list_tweets


def extract_normal_tweet(entry, users):
    if 'content' in entry and 'itemContent' in entry['content']:
        item_content = entry['content']['itemContent']
        if 'tweet_results' in item_content and 'result' in item_content['tweet_results']:
            legacy = item_content['tweet_results']['result']['legacy']
            if legacy is not None:
                user = list(filter(lambda x: x['rest_id'] == legacy['user_id_str'], users))
                created_at = legacy['created_at']
                full_text = legacy['full_text']
                id_str = legacy['id_str']
                max_res = ""
                return {
                    'username': user[0]['username'],
                    'created_at': created_at,
                    'full_text': full_text,
                    'id': id_str,
                    'attachment': max_res
                }


def extract_tweet_replies(entry, users):
    tweet_and_replies: dict
    if 'content' in entry and 'items' in entry['content']:
        items = entry['content']['items']
        for count, item in enumerate(items):
            item_content = item['item']['itemContent']
            if 'tweet_results' in item_content and 'result' in item_content['tweet_results']:
                legacy = item_content['tweet_results']['result']['legacy']
                if legacy is not None:
                    if count == 0:
                        user = list(filter(lambda x: x['rest_id'] == legacy['user_id_str'], users))
                        created_at = legacy['created_at']
                        full_text = legacy['full_text']
                        id_str = legacy['id_str']
                        max_res = ""
                        tweet_and_replies = {
                            'username': user[0]['username'],
                            'created_at': created_at,
                            'full_text': full_text,
                            'id': id_str,
                            'attachment': max_res,
                            'replies': []
                        }
                    else:
                        user = list(filter(lambda x: x['rest_id'] == legacy['user_id_str'], users))
                        created_at = legacy['created_at']
                        full_text = legacy['full_text']
                        id_str = legacy['id_str']
                        tweet_and_replies['replies'].append({
                            'username': user[0]['username'],
                            'created_at': created_at,
                            'full_text': full_text,
                            'id': id_str,
                        })
    return tweet_and_replies


def get_data():
    scraper = Scraper(cookies={
        "ct0": os.environ.get("TWITTER_CT0"),
        "auth_token": os.environ.get("TWITTER_AUTH_TOKEN"),

    }, debug=1, save=False)

    users = scraper.users([user['username'] for user in twitter_accounts])

    users_id = get_rest_ids(users)

    tweets = scraper.tweets([user['rest_id'] for user in users_id], limit=1)

    result = []
    for tweet in tweets:
        result.append(print_tweets(tweet, users_id))

    return result


def get_date(item):
    return datetime.datetime.strptime(item['created_at'], '%a %b %d %H:%M:%S %z %Y')


def find_account_by_username(username):
    for account in twitter_accounts:
        if account['username'] == username:
            return account


def replace_placeholders(template_file, replacements, output_file):
    with open(template_file, 'r') as file:
        template = file.read()

    for placeholder, value in replacements.items():
        template = template.replace('{' + placeholder + '}', value)

    with open(output_file, 'w') as file:
        file.write(template)


def add_is_police(item):
    item["is_police"] = False
    return item


if __name__ == '__main__':
    result = get_data()
    flat_result = [item for sublist in result for item in sublist if item is not None]
    flat_result.sort(key=get_date, reverse=True)
    print("total twitter news: " + str(len(flat_result)))
    twitter_account_data = []
    print(f'saving tweets ..')
    for i in range(len(flat_result)):
        twitter_account_data = find_account_by_username(flat_result[i]['username'])
        save_db({
            "username": flat_result[i]['username'],
            "tweets": flat_result[i],
            "prefix": twitter_account_data['prefix'],
            "suffix": twitter_account_data['suffix']
        })
    print("tweets saved ...")
    print("getting stored tweets ...")
    saved_tweets = list(map(add_is_police, get_tweets_db()))
    print("tweets: " + str(len(saved_tweets)))
    print("finishing getting stored tweets ...")
    print("Getting Police News")
    fetched_police_news = []
    for category in list_categories:
        print(category)
        fetched_police_news.append(get_police_news(category["category_name"], category["police_municipalities"]))

    print(len(fetched_police_news[0]),len(fetched_police_news[1]))


    flat_fetched_police_news = [item for sublist in fetched_police_news for item in sublist]


    merged_list = saved_tweets + flat_fetched_police_news
    print(len(merged_list))

    sorted_list = sorted(merged_list, key=lambda x: x.get("pub_date"), reverse=True)


    print("building RSS ...")
    for i in range(len(sorted_list)):
        if show_items is not None and all(item == show_items for item in number_acc):
            break

        for index in range(len(list_categories)):
            if number_acc[index] != show_items:
                category = list_categories[index]
                if sorted_list[i]["is_police"] is False or (
                        sorted_list[i]["is_police"] is True and sorted_list[i]["category"] == category[
                    "category_name"]):


                    convert_to_RSS(sorted_list[i], category['keywords'], category["negative_keywords"],
                                   feed_generators[index], category['category_name'], sorted_list[i]["is_police"])

                    for i in range(len(list_categories)):
                        category = list_categories[i]
                        feed_list = feed_generators[i].entry()
                        feed_generators[i].entry(sorted(feed_list, key=lambda x: x.pubDate(), reverse=True),
                                                 replace=True)
                        feed_generators[i].rss_str(pretty=True)
                        feed_generators[i].rss_file(f'./rss/{category["category_name"]}_rss.xml')
                        replaces = {
                            "category_name": category["category_name"],
                            "category_name_uppercase": category["category_name"].capitalize(),
                            "title": category["page_title"],
                            "title_horizontal": category["page_title_horizontal"],
                        }
                        replace_placeholders("templates/template_vertical.html", replaces,
                                             f"./web-pages/{category['category_name']}.html")
                        replace_placeholders("templates/template_horizantal.html", replaces,
                                             f"./web-pages/{category['category_name']}_horizontal.html")
                        replace_placeholders("templates/template.js", replaces,
                                             f"./web-pages/{category['category_name']}.js")

print("Job finished ...")
print("CLOSING INFOKANAL SCRAPPER ...")
