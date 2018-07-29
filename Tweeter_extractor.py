import tweepy
import json
from pymongo import MongoClient
import pymongo
from bson.json_util import dumps

# Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)

conn = "mongodb://[tanja.nyberg@outlook.com:Griesheim2002@]ds259241.mlab.com[:59241/heroku_18k0ln37]"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.twitter

tweets = db.tweets





# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(),wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# In[2]:

def scrape_tweets(): 
    db.tweets.drop()
    target_terms = ("@Reagan_Airport", "@NorfolkAirport","@Dulles_Airport", "@BWI_Airport",\
                    "@Flack4RIC","@PHLAirport","@FlyHIA")
    for target in target_terms:
        oldest_tweet = None
        public_tweets = api.search(target,count=2,max_id=oldest_tweet,tweet_mode='extended')
        for tweet in public_tweets['statuses']:
            tweets.insert_one(tweet)

        
