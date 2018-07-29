

from flask import Flask, render_template, redirect,request, url_for
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId
import Tweeter_extractor
from flask_bootstrap import Bootstrap
from config import(user,password)




# create instance of Flask app
app = Flask(__name__)

bootstrap = Bootstrap(app)

conn = 'mongodb://[user:password@]40ds259241.mlab.com:59241/heroku_18k0ln37'
client = pymongo.MongoClient(conn)


# Pass connection to the pymongo instance.



# Connect to a database. Will create one if not already available.
db =client.twitter

tweets=db.twitter

db.tweets.drop()



@app.route('/')
def index():
    
    datat =list(db.tweets.find())
    
    
    return render_template("index.html", datat=datat)




   

@app.route("/scrape")
def scrape():
    
    
    datat = db.tweets
    tweet_info = Tweeter_extractor.scrape_tweets()
    
    print(tweet_info)
     # Run scraped functions
    
    
    url="https://github.com/TanjaNY/GWU-Bootcamp-Project02/tree/master/templates"
    
     # Redirect back to home page 
    return redirect(url, code=302)
    #return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)





