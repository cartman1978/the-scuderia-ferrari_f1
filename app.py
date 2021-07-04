import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# MongoDb collection variables
user_coll = mongo.db.users
cars_coll = mongo.db.cars


@app.route("/")
def get_cars():
    """
    Function to render the home page and shows the 
    the existing cars. Newest cars are shown first
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    cars = cars_coll.find().sort('_id', -1)
    return render_template("cars.html", cars=cars, username=username) 



@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function to allow user to register at the website
    Check if username exists in db
    Redirect user to the dashboard
    """
    
    # Check if user is already logged in
    if 'user' in session:
        flash('You are already Registered')
        return redirect(url_for(get_cars))
    
    if request.method == "POST":
        
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))
        
        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))
        
        
        mongo.db.users.insert_one({
            'username': username,
            'password': password})
        
        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Account Registration Successfull!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows user to sign in with username and password
    Redirects user to profile
    """
    if request.method == "POST":
        # check if username exist in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # check if hashed password matches with user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))
        
        else:
            # invalid username
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))
        
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    cars = list(mongo.db.cars.find().sort('_id', 1))
    if session["user"]:
        return render_template("profile.html", username=username, cars=cars)
    
    return redirect(url_for("login"))



@app.route("/logout")
def logout():
    """
    Allows the user to log out
    Takes user back to home
    """
    # rmove user from session cookies
    flash("You're now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/addcar", methods=["GET", "POST"])
def addcar():
    if request.method == "POST":
        cars = {
            "car_image": request.form.get("car_image"),
            "car_year": request.form.get("car_year"),
            "car_name": request.form.get("car_name"),
            "car_design": request.form.get("car_design"),
            "car_driver1": request.form.get("car_driver1"),
            "car_driver2": request.form.get("car_driver2"),
            "spec_engine": request.form.get("spec_engine"),
            "car_power": request.form.get("car_power"),
            "trasmission": request.form.get("trasmission"),
            "races": request.form.get("races"),
            "wins": request.form.get("wins"),
            "podiums": request.form.get("podiums"),
            "poles": request.form.get("poles"),
            "fast_laps": request.form.get("fast_laps"),
            "constructor_champ": request.form.get("constructor_champ"),
            "drivers_champ": request.form.get("drivers_champ"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }

        
        mongo.db.cars.insert_one(cars)
        flash("Car Successfully Added")
        return redirect(url_for("get_cars"))
    return render_template("addcar.html")


@app.route("/editcar/<car_id>", methods=["GET", "POST"])
def editcar(car_id):
    if request.method == "POST":
        submit = {
            "car_image": request.form.get("car_image"),
            "car_year": request.form.get("car_year"),
            "car_name": request.form.get("car_name"),
            "car_design": request.form.get("car_design"),
            "car_driver1": request.form.get("car_driver1"),
            "car_driver2": request.form.get("car_driver2"),
            "spec_engine": request.form.get("spec_engine"),
            "car_power": request.form.get("car_power"),
            "trasmission": request.form.get("trasmission"),
            "races": request.form.get("races"),
            "wins": request.form.get("wins"),
            "podiums": request.form.get("podiums"),
            "poles": request.form.get("poles"),
            "fast_laps": request.form.get("fast_laps"),
            "constructor_champ": request.form.get("constructor_champ"),
            "drivers_champ": request.form.get("drivers_champ"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }

        
        mongo.db.cars.update({"_id": ObjectId(car_id)}, submit)
        flash("Car Successfully Updated")

    car = mongo.db.cars.find_one({"_id": ObjectId(car_id)})
    return render_template("editcar.html", car=car)


@app.route("/deletecar/<car_id>", methods=["GET", "POST"])
def deletecar(car_id):
    mongo.db.cars.remove({"_id": ObjectId(car_id)})
    flash("Car Successfully Deleted")
    return redirect(url_for("get_cars", car_id=car_id))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)