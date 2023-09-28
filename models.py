from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_year = db.Column(db.String(4), nullable=True)
    car_image = db.Column(db.String(255), nullable=True)
    car_name = db.Column(db.String(255), nullable=True)
    car_design = db.Column(db.String(255), nullable=True)
    car_driver_1 = db.Column(db.String(255), nullable=True)
    car_driver_2 = db.Column(db.String(255), nullable=True)
    spec_engine = db.Column(db.String(255), nullable=True)
    car_power = db.Column(db.String(255), nullable=True)
    trasmission = db.Column(db.String(255), nullable=True)
    races = db.Column(db.String(255), nullable=True)
    wins = db.Column(db.String(255), nullable=True)
    podiums = db.Column(db.String(255), nullable=True)
    poles = db.Column(db.String(255), nullable=True)
    fast_laps = db.Column(db.String(255), nullable=True)
    constructor_champ = db.Column(db.String(255), nullable=True)
    drivers_champ = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=True)