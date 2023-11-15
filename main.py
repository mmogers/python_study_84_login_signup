from flask import Flask, request, redirect, render_template
from replit import db

app = Flask(__name__, static_url_path='/static')

# Check if the database is initialized, and initialize it if not
if "users" not in db:
    db["users"] = {}

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginprocess', methods=["POST"])
def loginprocess():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in db["users"] and db["users"][username]["password"] == password:
        return "Hello"
    else:
        return "Not found"

@app.route('/process', methods=["POST"])
def process():
    form = request.form
    username = form.get("username")
    password = form.get("password")
    name = form.get("name")

    # Store user data in the "users" dictionary
    db["users"][username] = {"username": username, "password": password, "name": name}

    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
