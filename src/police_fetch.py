import feedparser
from feedgen.feed import FeedGenerator
from datetime import datetime
import pytz
import re
import os
import time
from helpers import check_date_is_day, retrieve_random_image
import urllib
import requests

def format_time_to_HHMM(input_time):
    """
    Converts a string representing a date and time to 'HH:MM' format.
    If input_time is None or cannot be parsed, returns None.
    """
    if input_time is None:
        return None
    try:
        # Parse input string into datetime object
        parsed_datetime = datetime.fromisoformat(input_time[:19])  # Truncate microseconds and timezone info
        return parsed_datetime.strftime('%H:%M')
    except Exception as e:
        print(f"Error converting time: {e}")
        return None


def convert_to_oslo_timezone(input_time):
    """
    Converts a string representing a date and time to Oslo timezone.
    If input_time is None or cannot be parsed, returns None.
    """
    if input_time is None:
        return None
    try:
        # Parse input string into datetime object
        parsed_datetime = datetime.fromisoformat(input_time[:19])  # Truncate microseconds and timezone info

        # Define Oslo timezone
        oslo_timezone = pytz.timezone('Europe/Oslo')

        # Convert datetime object to Oslo timezone
        oslo_datetime = parsed_datetime.astimezone(oslo_timezone)

        return oslo_datetime
    except Exception as e:
        print(f"Error converting time: {e}")
        return None


def get_police_news(category_name: str, police_municipalities: list[str]):
    encoded_municipalities = [urllib.parse.quote(m) for m in police_municipalities]


    police_feed_url = "https://api.politiet.no/politiloggen/v1/messages"
    params = {
        "Districts": "SørVest,Vest",
        "Municipalities": ','.join(encoded_municipalities),
        "Take": 50
    }

    response = requests.get(police_feed_url, params=params)
    print(response.url)
    result = response.json()
    print(result)

    extracted_items = []

    oslo_timezone = pytz.timezone('Europe/Oslo')

    for news_data in result["data"]:
        description = news_data["text"]

        username = f'politietsorvest'

        municipality = news_data["municipality"]

        area = news_data["area"]

        time_formatted = format_time_to_HHMM(news_data["createdOn"])

        tweet_body_rss = f"SISTE FRA POLITIET ({time_formatted}): #{municipality} #{area} {description} (POLITIET/RADIO HAUGALAND)"

        oslo_datetime = convert_to_oslo_timezone(news_data["createdOn"])

        thumbnail = retrieve_random_image(username, oslo_datetime)

        id = news_data["id"]

        link = 'https://www.politiet.no/politiloggen/hendelse/#/' + id

        item = {
            # '_id': ObjectId(),
            'username': username,
            'id': id,
            'tweet_body': description,
            'tweet_body_rss': tweet_body_rss,
            'thumbnail': thumbnail,
            'pub_date': oslo_datetime.timestamp(),  # Get the timestamp of oslo_datetime
            'link': link,
            'replies': None,
            'is_police': True,
            'category': category_name
        }

        extracted_items.append(item)

    return extracted_items
