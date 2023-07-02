from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING")


class TweetManager:
    def __init__(self):
        self.client = MongoClient(CONNECTION_STRING)
        self.db = self.client['infokanal']
        self.collection = self.db['tweets']

    def save_tweet(self, tweet):
        self.collection.insert_one(tweet)

    def get_tweets(self):
        return list(self.collection.find())

    def check_tweet_exist(self, tweet_id):
        tweet = self.collection.find_one({"id": tweet_id})
        return True if tweet else False
