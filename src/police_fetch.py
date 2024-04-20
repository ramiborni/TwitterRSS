import feedparser
from feedgen.feed import FeedGenerator
from datetime import datetime
import pytz
import re
import os
import time
from helpers import check_date_is_day, retrieve_random_image
import urllib


def format_time_to_HHMM(struct_time):
    """
    Converts a time.struct_time object to a string formatted as 'HH:MM'.
    If struct_time is None, returns None.
    """
    if struct_time is None:
        return None
    try:
        # Create datetime instance directly from struct_time using datetime.datetime
        published_datetime = datetime(*struct_time[:6])
        return published_datetime.strftime('%H:%M')
    except Exception as e:
        print(f"Error converting time: {e}")
        return None


def get_police_news(category_name: str, police_municipalities: list[str]):
    encoded_municipalities = [urllib.parse.quote(m) for m in police_municipalities]

    police_feed_url = 'https://api.politiet.no/politiloggen/v1/rss?districts=S%C3%B8rVest,Vest&municipalities=' + ",".join(
        encoded_municipalities)

    print(police_feed_url)

    police_feed = feedparser.parse(police_feed_url)

    extracted_items = []

    oslo_timezone = pytz.timezone('Europe/Oslo')

    for entry in police_feed.entries:
        title = entry.title
        description = entry.get("summary", "")
        username = f'politietsorvest'
        tweet_body = description

        time_formatted = format_time_to_HHMM(entry.published_parsed)

        tweet_body_rss = f"SISTE FRA POLITIET ({time_formatted}): {description} (POLITIET/RADIO HAUGALAND)"

        utc_datetime = datetime.fromtimestamp(time.mktime(entry.published_parsed))
        oslo_datetime = utc_datetime.astimezone(oslo_timezone)

        thumbnail = retrieve_random_image(username, oslo_datetime)

        item = {
            # '_id': ObjectId(),
            'username': username,
            'id': entry.id.replace('https://www.politiet.no/politiloggen/hendelse/#/', '').split('/')[0],
            'tweet_body': tweet_body,
            'tweet_body_rss': tweet_body_rss,
            "title": title,
            'thumbnail': thumbnail,
            'pub_date': oslo_datetime.timestamp(),  # Get the timestamp of oslo_datetime
            'link': entry.link,
            'replies': None,
            'is_police': True,
            'category': category_name
        }

        extracted_items.append(item)

    return extracted_items
