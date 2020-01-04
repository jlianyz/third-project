import os
from flask import Flask, render_template, redirect, request, url_for
import pymongo
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__) 

app.config["MONGO_DBNAME"] = 'myDatabase'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
conn = pymongo.MongoClient(app.config["MONGO_URI"])
DATABASE_NAME = "myDatabase"
COLLECTION_NAME = "products"
COLLECTION_NAME2 = "types"
COLLECTION_NAME3 = "purpose"
COLLECTION_NAME4 = "origin"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
