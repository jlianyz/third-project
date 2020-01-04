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


@app.route('/list_products')
def list_products():
    type = request.args.get('type')
    purpose = request.args.get('purpose')
    origin = request.args.get('origin')
    criteria= {} 
    
    if type and type != 'Type':
        criteria['type'] = type
    else:
        type = 'Type'
        
    if purpose and purpose != 'Purpose':
        criteria['purpose'] = purpose
    else:
        purpose ='Purpose'
        
    if origin and origin != 'Origin':
        criteria['origin'] = origin
    else:
        origin = 'Origin'
        
        
    products = conn[DATABASE_NAME][COLLECTION_NAME].find(criteria)
    print(products)
    types = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    purposes = conn[DATABASE_NAME][COLLECTION_NAME3].find()
    origins = conn[DATABASE_NAME][COLLECTION_NAME4].find()
    return render_template("list_products.html", 
                           products=products,type=type, purpose=purpose, origin=origin, types=types, purposes=purposes, origins=origins)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
