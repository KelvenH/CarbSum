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
        flash('''Sign-up was successful. Welcome to CarbSum!
              We hope you find this a helpful aid to
              support your carb counting''')
        return redirect(url_for("dashboard", username=session["user"]))
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
                return redirect(url_for("dashboard", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signIn"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signIn"))

    return render_template("signin.html")


# Dashboard
@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": username})

    if user:
        session['admin_role'] = user['admin_role']

    if 'user' in session:
        return render_template("dashboard.html", username=user["username"])

    return redirect(url_for("signIn"))


# Sign Out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have signed-out successfully")
    session.pop("user")
    session.pop("admin_role")
    return redirect(url_for("home"))


# Quick Calc
@app.route("/quick_calc")
def quick_calc():
    return render_template("quickcalc.html")


# User Content

# User Search
@app.route("/user_search", methods=["GET", "POST"])
def user_search():
    user_query = request.form.get("user_query")
    foods = list(mongo.db.foods.find({"$text": {"$search": user_query}}))
    return render_template("find_foods.html", foods=foods)


# Find Food Items
@app.route("/find_foods")
def find_foods():
    foods = list(mongo.db.foods.find().sort("food_title", 1))
    return render_template("find_foods.html", foods=foods)


# Search Categories
@app.route("/search_categories", methods=["GET", "POST"])
def search_categories():
    categories = mongo.db.food_categories.find().sort("cat_name", 1)

    if request.method == "POST":
        foods = list(mongo.db.foods.find(
            {"cat_name": request.form.get("find-cat-name")}))
        return render_template("search_categories.html",
                               categories=categories, foods=foods)

    foods = list(mongo.db.foods.find().sort("food_title", 1))
    return render_template("search_categories.html",
                           categories=categories, foods=foods)


# View Food Card (All Global + User Created)
@app.route("/user_view_food/<food_id>")
def user_view_food(food_id):
    food = mongo.db.foods.find_one({"_id": ObjectId(food_id)})
    return render_template("food_card.html", food=food)


# Create New Food (User Created)
@app.route("/add_userfood", methods=["GET", "POST"])
def add_userfood():
    if request.method == "POST":
        created_by = "admin" if session['admin_role'] else session["user"],
        status = "global" if session['admin_role'] else "private"
        food = {
            "food_title": request.form.get("add-food-title"),
            "food_subtitle": request.form.get("add-food-subtitle"),
            "cat_name": request.form.get("add-cat-name"),
            "portion_desc": request.form.get("add-portion-descrip"),
            "portion_unit": request.form.get("add-portion-unit"),
            "portion_size": float(request.form.get("add-portion-size")),
            "portion_carbs": float(request.form.get("add-carbs-per-portion")),
            "carbs_per_100g": float(request.form.get("add-carbs-per100")),
            "base_carbs": float(request.form.get("add-carbs-per-gram")),
            "carb_source": request.form.get("add-carbs-source"),
            "tag": request.form.getlist("add-tag-name"),
            "created_by": str(created_by[0]),
            "status": status
        }
        mongo.db.foods.insert_one(food)
        flash("New Food Entry Added")
        return redirect(url_for("dashboard", username=session["user"]))

    categories = mongo.db.food_categories.find().sort("cat_name", 1)
    tags = mongo.db.tags.find().sort("tag_name", 1)
    return render_template("add_food.html", categories=categories, tags=tags)


# User View Own Foods (User Created)
@app.route("/my_foods")
def my_foods():
    foods = list(mongo.db.foods.find())
    return render_template("myfoods.html", foods=foods)


# User Search Own Foods (User Created)
@app.route("/user_search_my_foods", methods=["GET", "POST"])
def user_search_my_foods():
    user_query = request.form.get("user_query")
    foods = list(mongo.db.foods.find({"$text": {"$search": user_query}}))
    return render_template("myfoods.html", foods=foods)


# Update Own Food (User Created)
@app.route("/edit_my_food/<food_id>", methods=["GET", "POST"])
def edit_my_food(food_id):
    if request.method == "POST":
        submit = {
            "food_title": request.form.get("edit-food-title"),
            "food_subtitle": request.form.get("edit-food-subtitle"),
            "cat_name": request.form.get("edit-cat-name"),
            "portion_desc": request.form.get("edit-portion-descrip"),
            "portion_unit": request.form.get("edit-portion-unit"),
            "portion_size": float(request.form.get("edit-portion-size")),
            "portion_carbs": float(request.form.get("edit-carbs-per-portion")),
            "carbs_per_100g": float(request.form.get("edit-carbs-per100")),
            "base_carbs": float(request.form.get("edit-carbs-per-gram")),
            "carb_source": request.form.get("edit-carbs-source"),
            "tag": request.form.getlist("edit-food-tag"),
            "created_by": request.form.get("edit-food-createdby"),
            "status": request.form.get("edit-food-status")
        }

        mongo.db.foods.update({"_id": ObjectId(food_id)}, submit)
        flash("Food Item Successfully Updated")
        return redirect(url_for("my_foods"))

    food = mongo.db.foods.find_one({"_id": ObjectId(food_id)})
    categories = mongo.db.food_categories.find().sort("cat_name", 1)
    tags = mongo.db.tags.find().sort("tag_name", 1)
    return render_template("edit_food.html",
                           food=food, categories=categories, tags=tags)


# Delete Own Food (User Created)
@app.route("/delete_my_food/<food_id>")
def delete_my_food(food_id):
    mongo.db.foods.delete_one({"_id": ObjectId(food_id)})
    flash("Food entry has been successfully deleted")
    return redirect(url_for("my_foods"))


# ADMIN Restricted Content

# Admin Search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    foods = list(mongo.db.foods.find({"$text": {"$search": query}}))
    return render_template("manage_foods.html", foods=foods)


# Foods - Create
@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "POST":
        created_by = "admin" if session['admin_role'] else session["user"],
        status = "global" if session['admin_role'] else "private"
        food = {
            "food_title": request.form.get("add-food-title"),
            "food_subtitle": request.form.get("add-food-subtitle"),
            "cat_name": request.form.get("add-cat-name"),
            "portion_desc": request.form.get("add-portion-descrip"),
            "portion_unit": request.form.get("add-portion-unit"),
            "portion_size": float(request.form.get("add-portion-size")),
            "portion_carbs": float(request.form.get("add-carbs-per-portion")),
            "carbs_per_100g": float(request.form.get("add-carbs-per100")),
            "base_carbs": float(request.form.get("add-carbs-per-gram")),
            "carb_source": request.form.get("add-carbs-source"),
            "tag": request.form.getlist("add-tag-name"),
            "created_by": str(created_by[0]),
            "status": status
        }
        mongo.db.foods.insert_one(food)
        flash("New Food Entry Added")
        return redirect(url_for("get_foods"))

    categories = mongo.db.food_categories.find().sort("cat_name", 1)
    tags = mongo.db.tags.find().sort("tag_name", 1)
    return render_template("add_food.html", categories=categories, tags=tags)


# Foods - Read
@app.route("/get_foods")
def get_foods():
    foods = list(mongo.db.foods.find())
    return render_template("manage_foods.html", foods=foods)


# Foods - Update
@app.route("/edit_food/<food_id>", methods=["GET", "POST"])
def edit_food(food_id):
    if request.method == "POST":
        submit = {
            "food_title": request.form.get("edit-food-title"),
            "food_subtitle": request.form.get("edit-food-subtitle"),
            "cat_name": request.form.get("edit-cat-name"),
            "portion_desc": request.form.get("edit-portion-descrip"),
            "portion_unit": request.form.get("edit-portion-unit"),
            "portion_size": float(request.form.get("edit-portion-size")),
            "portion_carbs": float(request.form.get("edit-carbs-per-portion")),
            "carbs_per_100g": float(request.form.get("edit-carbs-per100")),
            "base_carbs": float(request.form.get("edit-carbs-per-gram")),
            "carb_source": request.form.get("edit-carbs-source"),
            "tag": request.form.getlist("edit-food-tag"),
            "created_by": request.form.get("edit-food-createdby"),
            "status": request.form.get("edit-food-status")
        }

        mongo.db.foods.update({"_id": ObjectId(food_id)}, submit)
        flash("Food Item Successfully Updated")
        return redirect(url_for("get_foods"))

    food = mongo.db.foods.find_one({"_id": ObjectId(food_id)})
    categories = mongo.db.food_categories.find().sort("cat_name", 1)
    tags = mongo.db.tags.find().sort("tag_name", 1)
    return render_template("edit_food.html",
                           food=food, categories=categories, tags=tags)


# Foods - Delete
@app.route("/delete_food/<food_id>")
def delete_food(food_id):
    mongo.db.foods.delete_one({"_id": ObjectId(food_id)})
    flash("Food entry has been successfully deleted")
    return redirect(url_for("get_foods"))


# Categories - Create
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "cat_name": request.form.get("add-category-name")
        }
        mongo.db.food_categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Categories - Read
@app.route("/get_categories")
def get_categories():
    categories = mongo.db.food_categories.find().sort("cat_name", 1)
    return render_template("manage_categories.html", categories=categories)


# Categories - Update
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "cat_name": request.form.get("edit-category-name")
        }

        mongo.db.food_categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.food_categories.find_one(
        {"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Categories - Delete
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.food_categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category has been successfully deleted")
    return redirect(url_for("get_categories"))


# Tags - Create
@app.route("/add_tag", methods=["GET", "POST"])
def add_tag():
    if request.method == "POST":
        tag = {
            "tag_name": request.form.get("add-tag-name")
        }
        mongo.db.tags.insert_one(tag)
        flash("New Tag Added")
        return redirect(url_for("get_tags"))

    return render_template("add_tag.html")


# Tags - Read
@app.route("/get_tags")
def get_tags():
    tags = mongo.db.tags.find()
    return render_template("manage_tags.html", tags=tags)


# Tags - Update
@app.route("/edit_tag/<tag_id>", methods=["GET", "POST"])
def edit_tag(tag_id):
    if request.method == "POST":
        submit = {
            "tag_name": request.form.get("edit-tag-name")
        }

        mongo.db.tags.update({"_id": ObjectId(tag_id)}, submit)
        flash("Tag Successfully Updated")
        return redirect(url_for("get_tags"))

    tag = mongo.db.tags.find_one({"_id": ObjectId(tag_id)})
    return render_template("edit_tag.html", tag=tag)


# Tags - Delete
@app.route("/delete_tag/<tag_id>")
def delete_tag(tag_id):
    mongo.db.tags.delete_one({"_id": ObjectId(tag_id)})
    flash("Tag has been successfully deleted")
    return redirect(url_for("get_tags"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)   # change status to False prior to deployment
