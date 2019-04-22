

from flask import Flask, render_template, redirect,request, url_for
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId
import Tweeter_extractor
from flask_bootstrap import Bootstrap
from config import (database_user,
                   database_pass,
                   databasename)
#C:\path\to\app>set FLASK_APP=app.py
#flask run
#Open your browser. Go to http://127.0.0.1:5000/

# create instance of Flask app
app = Flask(__name__)

bootstrap = Bootstrap(app)

#conn = 'mongodb://localhost:27017'

conn ='mongodb://celasson:Yorktown2008@ds157895.mlab.com:57895/heroku_g12ldwwq'
client = pymongo.MongoClient(conn)



# Pass connection to the pymongo instance.



# Connect to a database. Will create one if not already available.
db =client.heroku_g12ldwwq

collection=db.tweets


#db.tweets.drop()



@app.route('/')
def index():
    
    docs = list(db.tweets.find())
 
    
    return render_template("index.html", docs=docs)




   

@app.route("/scrape")
def scrape_tweets():
    
    #entries = mongo.db.mission_to_mars
    tweet_info = mongo.db.tweets.scrape_tweets()
    
    
     # Run scraped functions
url='https://statairport.herokuapp.com/'
    
    
     # Redirect back to home page 
   # return redirect(url, code=307)
return redirect(url, code=302)

if __name__ == "__main__":
    app.run(debug=True)





