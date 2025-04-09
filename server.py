from flask import Flask, render_template, request
import json
from config import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.get("/tests")
def test():
    return "This is a test endpoint"


@app.get("/home")
def home():
    return "Welcome to the Home page!"


@app.get("/users")
def users():
    return "<p>Hello, world!</p>"


@app.get("/api/about")
def about():
    name = {"name" : "Rafael Cabrera"}
    return name


@app.get("/api/students")
def students():
    students = ["Jeffrey", "George", "Nar", "Rafael", "Isai" "Erick"]
    return students


@app.get("/contact")
def contact_api():
    user_name = "Pam"
    age = 25
    return render_template("contact.html", name=user_name, age=age)


products = []


@app.get("/api/products")
def get_products():
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

#POST
@app.post("/api/products")
def post_products():
    item = request.get_json()
    print(item)

    db.products.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))

# PUT
@app.put("/api/products/<int:index>")
def put_products(index):
    updated_item = request.get_json()
    if len(products) > index >= 0:
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "Index does not exist"

#DELETE
@app.delete("/api/products/<int:index>")
def delete_product(index):
    delete_item = request.get_json()
    if 0<= index < len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "That item does not exist"


@app.patch("/api/products/<int:index>")
def patch_product(index):
    patch_item = request.get_json()
    if 0<= index < len(products):
        products(index).update(patch_item)
        return json.dumps(products)
    else:
        return "That item does not exist"


@app.get("/greet/<name>")
def asd_api(name):
    
    print("Greet endpoint accessed")
    
    #return "Hello " + name
    return f"Hello {name}"



app.run(debug=True, port=8000)