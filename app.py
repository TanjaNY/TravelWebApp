

from flask import Flask, render_template, redirect,request, url_for
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId
import Tweeter_extractor
from flask_bootstrap import Bootstrap


# create instance of Flask app
app = Flask(__name__)

bootstrap = Bootstrap(app)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)



# Pass connection to the pymongo instance.



# Connect to a database. Will create one if not already available.
db =client.twitter

tweets=db.twitter

#db.tweets.drop()



@app.route('/')
def index():
    
    datat =db.tweets.find()
      
    
    
        
    print(datat)
    
    
    
    
    return render_template("index.html", datat=datat)




   

@app.route("/scrape")
def scrape():
    
    #entries = mongo.db.mission_to_mars
    tweet_info = tweets.scrape_tweets()
    
    
     # Run scraped functions
    
    url='https://tanjany.github.io/GWU-Bootcamp-Project02'
    
    
     # Redirect back to home page 
    return redirect(url, code=307)


if __name__ == "__main__":
    app.run(debug=True)





