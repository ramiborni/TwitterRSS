import feedparser
from feedgen.feed import FeedGenerator
from datetime import datetime
import pytz
import re
import os
import time

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




def get_police_news():
    police_feed_url = 'https://api.politiet.no/politiloggen/v1/rss?districts=S%C3%B8rVest,Vest&municipalities=Bokn,Bømlo,Etne,Fitjar,Haugesund,Karmøy,Sauda,Stord,Suldal,Sveio,Utsira,Tysvær,Vindafjord'
    police_feed = feedparser.parse(police_feed_url)

    extracted_items = []

    for entry in police_feed.entries:
        print(entry)
        title = entry.title
        description = entry.get("summary", "")
        username = f'politietsorvest'
        tweet_body = description

        time_formatted = format_time_to_HHMM(entry.published_parsed)

        tweet_body_rss = f"SISTE FRA POLITIET ({time_formatted}): {description} (POLITIET/RADIO HAUGALAND)"
        thumbnail = f''

        item = {
            #'_id': ObjectId(),
            'username': username,
            'id': entry.id.replace('https://www.politiet.no/politiloggen/hendelse/#/', '').split('/')[0],
            'tweet_body': tweet_body,
            'tweet_body_rss': tweet_body_rss,
            'thumbnail': thumbnail,
            'pub_date': datetime(*entry.published_parsed[:6]).timestamp(),
            'link': entry.link,
            'replies': None,
            'is_police': True
        }
        extracted_items.append(item)

    return extracted_items
