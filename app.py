

from flask import Flask, render_template, redirect,request, url_for
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap
import tweepy
import json
from bson.json_util import dumps

# Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)




# create instance of Flask app
app = Flask(__name__)

bootstrap = Bootstrap(app)




# Pass connection to the pymongo instance.
conn = "mongodb://heroku_g12ldwwq:e0kpf37iu52licms2rmqo1ajr2@ds113826.mlab.com:13826/heroku_g12ldwwq"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.heroku_g12ldwwq

collection = db.tweets




#db.tweets.drop()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(),wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

@app.route('/')
def index():
    
    datat =list(db.tweets.find())
    print(datat)
    
    
    return render_template("index.html")

@app.route("/scrape")
   
def scrape(): 
    db.tweets.drop()
    target_terms = ("@Reagan_Airport", "@NorfolkAirport","@Dulles_Airport", "@BWI_Airport",\
                    "@Flack4RIC","@PHLAirport","@FlyHIA")
    for target in target_terms:
        oldest_tweet = None
        public_tweets = api.search(target,count=2,max_id=oldest_tweet,tweet_mode='extended')
        for tweet in public_tweets['statuses']:
            tweets.insert_one(tweet)
    
        datat = db.tweets
        #tweet_info=Tweeter_extractor.scrape_tweets()
    
        #print(datat)
     # Run scraped functions
    
    
    url="https://statairport.herokuapp.com/"

 

   
    
     # Redirect back to home page 
    return redirect(url, code=302)
    #return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)





