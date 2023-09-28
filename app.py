import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# SQLAlchemy configurations
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("SECRET_KEY")
from models import db

db.init_app(app)




from models import User, Car  


@app.route("/")
def get_cars():
    cars = Car.query.order_by(desc(Car.id)).all()
    return render_template("pages/cars.html", cars=cars)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cars = Car.query.filter(Car.car_year.contains(query)).order_by(desc(Car.id)).all()
    return render_template("pages/cars.html", cars=cars)


@app.route("/register", methods=["GET", "POST"])
def register():
    if 'user' in session:
        flash('You are already Registered')
        return redirect(url_for(get_cars))

    if request.method == "POST":
        existing_user = User.query.filter_by(username=request.form.get("username").lower()).first()

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))

        user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        session["user"] = request.form.get("username").lower()
        flash("Account Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form.get("username").lower()).first()

        if user and check_password_hash(user.password, request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {}".format(request.form.get("username")))
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = User.query.filter_by(username=session["user"]).first()
    cars = Car.query.all()
    
    if session["user"]:
        return render_template('pages/profile.html', username=username, cars=cars)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You're now logged out")
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/addcar", methods=["GET", "POST"])
def addcar():
    if request.method == "POST":
        car = Car(
        car_image=request.form.get("car_image"),
        car_year=request.form.get("car_year"),
        car_name=request.form.get("car_name"),
        car_design=request.form.get("car_design"),
        car_driver_1=request.form.get("car_driver_1"),
        car_driver_2=request.form.get("car_driver_2"),
        spec_engine=request.form.get("spec_engine"),
        car_power=request.form.get("car_power"),
        trasmission=request.form.get("trasmission"),
        races=request.form.get("races"),
        wins=request.form.get("wins"),
        podiums=request.form.get("podiums"),
        poles=request.form.get("poles"),
        fast_laps=request.form.get("fast_laps"),
        constructor_champ=request.form.get("constructor_champ"),
        drivers_champ=request.form.get("drivers_champ"),
        description=request.form.get("description"),
        created_by=session["user"]
    )
    
        db.session.add(car)
        db.session.commit()
        flash("Car Successfully Added")
        return redirect(url_for("get_cars"))
    else:
        car = None
        return render_template("pages/addcar.html", car=car)
    



@app.route("/editcar/<int:car_id>", methods=["GET", "POST"])
def editcar(car_id):
    car = Car.query.get_or_404(car_id)
    
    if session["user"]:
        if request.method == "POST":
            car.car_image = request.form.get("car_image")
            car.car_year = request.form.get("car_year")
            car.car_name = request.form.get("car_name")
            car.car_design = request.form.get("car_design")
            car.car_driver_1 = request.form.get("car_driver_1")
            car.car_driver_2 = request.form.get("car_driver_2")
            car.spec_engine = request.form.get("spec_engine")
            car.car_power = request.form.get("car_power")
            car.trasmission = request.form.get("trasmission")
            car.races = request.form.get("races")
            car.wins = request.form.get("wins")
            car.podiums = request.form.get("podiums")
            car.poles = request.form.get("poles")
            car.fast_laps = request.form.get("fast_laps")
            car.constructor_champ = request.form.get("constructor_champ")
            car.drivers_champ = request.form.get("drivers_champ")
            car.description = request.form.get("description")
        
            car.created_by = session["user"]

            db.session.commit()
            flash("Car Successfully Updated")
            return redirect(url_for("get_cars"))
    else:
        flash("You don't have permission to edit this car")

    return render_template("pages/editcar.html", car=car)


@app.route("/deletecar/<int:car_id>", methods=["GET", "POST"])
def deletecar(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    flash("Car Successfully Deleted")
    return redirect(url_for("get_cars", car_id=car_id))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("/components/errors/404.html", error=error), 404


@app.errorhandler(500)
def something_went_wrong(error):
    return render_template("/components/errors/500.html", error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
