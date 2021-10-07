from flask import *
import pyrebase
import MathBot1
import pandas as pd

config = {
    "apiKey": "AIzaSyCis1HsZLVWRATo3bBDApgctASCvQpzZM0",
    "authDomain": "luciobot-9138b.firebaseapp.com",
    "databaseURL": "https://luciobot-9138b-default-rtdb.firebaseio.com",
    "projectId": "luciobot-9138b",
    "storageBucket": "luciobot-9138b.appspot.com",
    "messagingSenderId": "1063456209794",
    "appId": "1:1063456209794:web:2e5129d3d553e49a06ad9b",
    "measurementId": "G-YK6JP0S5EB"
}

# firebase.com
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# inicializador de flask
app = Flask(__name__)
app.secret_key = "hola"

# /index
@app.route("/", methods=["GET", "POST"])
def logIn():
    unsuccesful = "Please check your credentials."
    if request.method == "POST":
        email = request.form["name"]
        password = request.form["password"]
        session["user"] = email
        try:
            auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('upload'))
        except:
            return render_template("index.html", us=unsuccesful)
    else:
        return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" in session:
        return render_template("upload.html") 
    return render_template("index.html")

@app.route("/data", methods=["GET", "POST"])
def data():
    if "user" in session:
        unsuccesful = "The data entered is not correct."
        if request.method == "POST":
            path = request.files["uploadFile"]
            fee = request.form.get('fee', type=int)
            ryan = request.form.get('ryan', type=int)
            zane = request.form.get('zane', type=int)
            austin = request.form.get('austin', type=int)
            try:
                info = MathBot1.runMathBot(path,fee,ryan,zane,austin)
                return render_template("data.html", data=info)
            except:
                return render_template("upload.html", data=unsuccesful)
    return render_template("index.html")
