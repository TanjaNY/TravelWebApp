

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




# Pass connection to the pymongo instance.
conn = "mongodb://heroku_g12ldwwq:e0kpf37iu52licms2rmqo1ajr2@ds113826.mlab.com:13826/heroku_g12ldwwq"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.heroku_g12ldwwq

collection = db.tweets




db.tweets.drop()



@app.route('/')
def index():
    
    datat =list(db.tweets.find())
    print(datat)
    
    
    return render_template("index.html")

 

    url="https://statairport.herokuapp.com/"
    
     # Redirect back to home page 
    return redirect(url, code=302)
    #return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)





