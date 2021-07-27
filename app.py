import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Create Flask instance
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Route decorators
@app.route("/")
@app.route("/get_foods")
def get_foods():
    foods = mongo.db.foods.find()
    return render_template("foods.html", foods=foods)


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username {} taken, please try another".format(
                request.form.get("username"))) #Added display of the attempted username within Flash message, Acknowledgement codemy.com https://www.youtube.com/watch?v=4yaG-jFfePc
            return redirect(url_for("join"))

        join = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(join)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign-up was successful. Welcome to CarbSum! We hope you find this a helpful aid to support your carb counting")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("join.html")


@app.route("/signIn", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
        # check hashed password in db matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signIn"))

        else:
            #username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signIn"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    #grab the session user's username from db
    username =mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)   # change status to False prior to deployment
