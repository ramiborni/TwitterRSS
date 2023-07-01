from datetime import datetime, timedelta, timezone
from urllib.parse import quote_plus


def extract_data(latest_results, max_items, date_threshold=None):
    extracted_data = []

    for results in latest_results:
        for result in results:
            if result is None:
                continue
            tweet = result['globalObjects']['tweets']
            for tweet_id, tweet_data in tweet.items():
                full_text = tweet_data['full_text']
                created_at = tweet_data['created_at']
                username = result['globalObjects']['users'][str(tweet_data['user_id'])]['screen_name']
                tweet_link = f"https://twitter.com/{username}/status/{tweet_id}"

                if is_created_after(created_at, date_threshold):
                    extracted_data.append({
                        'full_text': full_text,
                        'created_at': created_at,
                        'username': username,
                        'tweet_link': tweet_link,
                        'id': tweet_id,
                        'attachment': None,
                    })
    sorted_data = sorted(extracted_data,
                         key=lambda x: datetime.strptime(x['created_at'], "%a %b %d %H:%M:%S %z %Y"),
                         reverse=True)

    unique_data = list({obj['full_text']: obj for obj in sorted_data}.values())

    if max_items is not None:
        return unique_data[:max_items]
    return unique_data


def is_created_after(created_at, date_threshold=None):
    if date_threshold is None:
        return True

    current_datetime = datetime.now(timezone.utc)
    threshold_datetime = current_datetime - timedelta(hours=int(date_threshold[:-1]))

    date_format = "%a %b %d %H:%M:%S %z %Y"
    created_at_datetime = datetime.strptime(created_at, date_format).replace(tzinfo=timezone.utc)

    return created_at_datetime > threshold_datetime
