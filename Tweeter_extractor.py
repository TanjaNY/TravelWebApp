import tweepy
import json
from pymongo import MongoClient
import pymongo
from bson.json_util import dumps

#Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                   access_token_secret,
                    database_user,
                   database_pass,
                   databasename)


#consumer_key="GmJPV7YJA0YzfnBmPDg8pkVMW"
#consumer_secret="ln2sMygoZhBQlvNAjv3GShpWC6lGIleDxie7HBwTN9HGPbbgym"
#access_token="987885617043464192-f7jBC47kNQ4gGcMyLBzRv9sD5GLC13R"
#access_token_secret="kNASDSEaz7zp5yL0FjdgNs04CsQgM0GmqoWmsZidAxWmA"


#conn='mongodb://celasson01:Yorktown2008.ds113826.mlab.com:13826/heroku_g12ldwwq'
#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(conn)

# Select database and collection to use
#db = client.tweets

#HOST = 'ds113826.mlab.com'
#PORT = 13826
#database_user = 'celasson'
#database_pass = 'Yorktown2008'
#databasename ='heroku_g12ldwwq'
#uri='mongodb://celasson01:Yorktown2008.ds113826.mlab.com:13826/heroku_g12ldwwq'

connection = pymongo.MongoClient('ds157895.mlab.com',57895)
db = connection[databasename]
db.authenticate(database_user, database_pass)



#tweets = db.heroku_g12ldwwq
tweets = db.tweets


#db.heroku_g12ldwwq.drop()
db.tweets.drop()



# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(),wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


# In[2]:


target_terms = ("@Reagan_Airport", "@NorfolkAirport","@Dulles_Airport", "@BWI_Airport",
                "@Flack4RIC", "@PHLAirport", "@FlyHIA")
for target in target_terms:
    oldest_tweet = None
    public_tweets = api.search(target,count=5,max_id=oldest_tweet,tweet_mode='extended')
    for tweet in public_tweets['statuses']:
        tweets.insert_one(tweet)

