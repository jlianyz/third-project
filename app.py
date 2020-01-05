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
COLLECTION_NAME2 = "types" # contains all the products types
COLLECTION_NAME3 = "purpose" # contains all the products' purposes
COLLECTION_NAME4 = "origin" # contains all the products countries
mongo = PyMongo(app)

# link to index page
@app.route('/')
def index():
    return render_template('index.html')

#link to list products lage
@app.route('/list_products')
def list_products():
    type = request.args.get('type')
    purpose = request.args.get('purpose')
    origin = request.args.get('origin')
    criteria= {} 
#search database using 3 criterias: type, purpose and origin    
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
        
# search through the following collections and display the products accordingly        
    products = conn[DATABASE_NAME][COLLECTION_NAME].find(criteria)
    print(products)
    types = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    purposes = conn[DATABASE_NAME][COLLECTION_NAME3].find()
    origins = conn[DATABASE_NAME][COLLECTION_NAME4].find()
    return render_template("list_products.html", 
                           products=products,type=type, purpose=purpose, origin=origin, types=types, purposes=purposes, origins=origins)

# for images, they are stored as their filename in mongodb
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

# these are used for the for loops in the dropdown menus
@app.route('/add_product') 
def add_product():
    types = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    purposes = conn[DATABASE_NAME][COLLECTION_NAME3].find()
    origins = conn[DATABASE_NAME][COLLECTION_NAME4].find()
    
    return render_template('add_product.html', types=types, purposes=purposes, origins=origins)

# get the information inputted in the form to insert into mongoDB    
@app.route('/add_product', methods=['POST'])
def insert_product():
    name = request.form.get('name')
    brand = request.form.get('brand')
    price = request.form.get('price')
    origin = request.form.get('origin')
    type = request.form.get('type')
    purpose = request.form.get('purpose')
    volume = request.form.get('volume')
    description = request.form.get('description')
    
    if "product_image" in request.files:
        product_image = request.files['product_image']
        mongo.save_file(product_image.filename, product_image)
    
    conn[DATABASE_NAME][COLLECTION_NAME].insert({
        "name" : name,
        "brand" : brand,
        "price" : price,
        "origin" : origin,
        "type" : type,
        "purpose" : purpose,
        "volume" : volume,
        "description" : description,
        "product_image_name" : product_image.filename
    })
    
    return redirect("/")

#link to the correct object id from the "products" collection
@app.route("/product_details/<product_id>")
def products_details(product_id):
    products = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        "_id":ObjectId(product_id)
    })
    return render_template("product_details.html", products=products)

# used to define the url for the edit products page
@app.route('/edit_product/<products_id>') 
def show_edit_product(products_id):
    types = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    purposes = conn[DATABASE_NAME][COLLECTION_NAME3].find()
    origins = conn[DATABASE_NAME][COLLECTION_NAME4].find()
    product = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        '_id': ObjectId(products_id)
    })
    return render_template('edit_product.html', product=product, types=types, purposes=purposes, origins=origins)
    
@app.route("/edit_product/<products_id>", methods=['POST'])
def process_edit_product(products_id):
    product = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        '_id': ObjectId(products_id)
    })
    
    name = request.form.get('name')
    brand = request.form.get('brand')
    price = request.form.get('price')
    type = request.form.get('type')
    purpose = request.form.get('purpose')
    origin = request.form.get('origin')
    volume = request.form.get('volume')
    description = request.form.get('description')
    print(request.files)
    if "product_image" in request.files and request.files['product_image'].filename != "": # ensure that if no image is added, existing one still shows
        product_image = request.files['product_image']
        image_filename = product_image.filename
        mongo.save_file(product_image.filename, product_image)
    else:
        image_filename = product['product_image_name']
    
    # update the mongoDB collection with the above form information    
    conn[DATABASE_NAME][COLLECTION_NAME].update({
        '_id':ObjectId(products_id)
    }, {
        "name" : name,
        "brand" : brand,
        "price" : price,
        "origin" : origin,
        "type" : type,
        "purpose" : purpose,
        "volume" : volume,
        "description" : description,
        "product_image_name" :image_filename
    })
    return redirect(url_for('list_products'))   

# to delete the product identified using the product id    
@app.route('/delete_product/<products_id>') 
def delete_product(products_id):
    products = conn[DATABASE_NAME][COLLECTION_NAME].remove({
        '_id': ObjectId(products_id)
        
    })
    return redirect(url_for('list_products'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
