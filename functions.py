from db import TweetManager

tweet_manager = TweetManager()

def save_filtered_data(data):
    if data is not None:
        tweet_manager.save_tweet(data)


def check_tweet_exist(id):
    return tweet_manager.check_tweet_exist(id)


def get_tweets_db():
    tweets_list = tweet_manager.get_tweets()
    return tweets_list