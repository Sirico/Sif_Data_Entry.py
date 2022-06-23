from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
import pandas as pd


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    SKU = db.Column(db.Integer, unique=True, nullable=False)
    Parent = db.Column(db.Boolean)
    Brand = db.Column(db.String(20), unique=True, nullable=False)
    Gender = db.Column(db.String(20), unique=True, nullable=False)
    Closure = db.Column(db.String(20), unique=True, nullable=False)
    Type = db.Column(db.String(20), unique=True, nullable=False)
    Colour = db.Column(db.String(20), unique=True, nullable=False)
    Country_Manu = db.Column(db.String(20), unique=True, nullable=False)
    Upper_Mat = db.Column(db.String(20), unique=True, nullable=False)
    Lining_Mat = db.Column(db.String(20), unique=True, nullable=False)
    Insole_Mat = db.Column(db.String(20), unique=True, nullable=False)
    Heel_Height = db.Column(db.Integer, unique=True, nullable=False)
    Weight = db.Column(db.Integer, unique=True, nullable=False)
    Height = db.Column(db.Integer, unique=True, nullable=False)
    Length = db.Column(db.Integer, unique=True, nullable=False)
    Depth = db.Column(db.Integer, unique=True, nullable=False)
    Purchase_Ord = db.Column(db.Integer, unique=True, nullable=False)
    Label = db.Column(db.String(20), unique=True, nullable=False)
    Kids_Sizes = db.Column(db.Integer, unique=True, nullable=False)
    Adult_Sizes = db.Column(db.Integer, unique=True, nullable=False)

# Data entry form to be submitted to database
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    Date = db.Column(db.DateTime, default=datetime.utcnow)
    SKU = db.Column(db.Integer, unique=True, nullable=False)
    Parent = db.Column(db.Boolean)
    Brand = db.Column(db.String(20), unique=True, nullable=False)
    Gender = db.Column(db.String(20), unique=True, nullable=False)
    Closure = db.Column(db.String(20), unique=True, nullable=False)
    Type = db.Column(db.String(20), unique=True, nullable=False)
    Colour = db.Column(db.String(20), unique=True, nullable=False)
    Country_Manu = db.Column(db.String(20), unique=True, nullable=False)
    Upper_Mat = db.Column(db.String(20), unique=True, nullable=False)
    Lining_Mat = db.Column(db.String(20), unique=True, nullable=False)
    Insole_Mat = db.Column(db.String(20), unique=True, nullable=False)
    Heel_Height = db.Column(db.Integer, unique=True, nullable=False)
    Weight = db.Column(db.Integer, unique=True, nullable=False)
    Height = db.Column(db.Integer, unique=True, nullable=False)
    Length = db.Column(db.Integer, unique=True, nullable=False)
    Depth = db.Column(db.Integer, unique=True, nullable=False)
    Purchase_Ord = db.Column(db.Integer, unique=True, nullable=False)
    Label = db.Column(db.String(20), unique=True, nullable=False)
    Kids_Sizes = db.Column(db.Integer, unique=True, nullable=False)
    Adult_Sizes = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
