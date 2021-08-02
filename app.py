  
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
@app.route("/home")
def home():
    return render_template("index.html")

# Registration
@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username {} taken, please try another".format(
                request.form.get("username")))
            return redirect(url_for("join"))

        join = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "admin_role": False
        }
        mongo.db.users.insert_one(join)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower(),
        flash("Sign-up was successful. Welcome to CarbSum! We hope you find this a helpful aid to support your carb counting")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("join.html")

# Sign In
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
                    return redirect(url_for("profile", username=session["user"]))
            
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signIn"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signIn"))

    return render_template("signin.html")

# Profile (Dashboard)
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": username})
    
    if user:
        session['admin_role'] = user['admin_role']

    if 'user' in session:
        return render_template("profile.html", username=user["username"])

    return redirect(url_for("signIn"))

# Sign Out
@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have signed-out successfully")
    session.pop("user")
    session.pop("admin_role")
    return redirect(url_for("home"))


# Quick Calc
@app.route("/quick_calc")
def quick_calc():
    return render_template("quickcalc.html")


# admin restricted content
@app.route("/get_foods")
def get_foods():
    foods = mongo.db.foods.find()
    return render_template("foods.html", foods=foods)


@app.route("/add_foods", methods=["GET", "POST"])
def add_foods():
    if request.method == "POST":
        food = {
            "cat_name": request.form.get("cat_name"),
            "food_title": request.form.get("cat_name"),
            "food_subtitle": request.form.get("cat_name"),
            "base_carbs": request.form.get("cat_name"),
            "tag": request.form.get("cat_name"),
            "temp": request.form.get("cat_name"),
        }
        mongo.db.foods.insert_one(food)
        flash("New Food Entry Added")
        return redirect(url_for("get_foods"))

    return render_template("add_foods.html")


@app.route("/get_categories")
def get_categories():
    categories = mongo.db.food_categories.find()
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/get_tags")
def get_tags():
    tags = mongo.db.tags.find()
    return render_template("tags.html", tags=tags)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)   # change status to False prior to deployment