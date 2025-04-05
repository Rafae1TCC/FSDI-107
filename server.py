from flask import Flask, render_template

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


@app.get("/greet/<name>")
def asd_api(name):
    
    print("Greet endpoint accessed")
    
    #return "Hello " + name
    return f"Hello {name}"

app.run(debug=True, port=8000)