from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin



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
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    Author = db.Column(db.String(20), unique=True, nullable=False)
    SKU = db.Column(db.Integer, unique=True, nullable=False)
    Parent = db.Column(db.Boolean)
    Brand = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.Integer, nullable=False)
    Closure = db.Column(db.Integer, nullable=False)
    Model = db.Column(db.Integer, nullable=False)
    Type = db.Column(db.Integer, nullable=False)
    Colour = db.Column(db.Integer, nullable=False)
    Country_Manu = db.Column(db.Integer, nullable=False)
    Upper_Mat = db.Column(db.Integer, nullable=False)
    Lining_Mat = db.Column(db.Integer, nullable=False)
    Insole_Mat = db.Column(db.Integer, nullable=False)
    Heel_Height = db.Column(db.Integer, nullable=False)
    Weight = db.Column(db.Integer, nullable=False)
    Height = db.Column(db.Integer, nullable=False)
    Length = db.Column(db.Integer, nullable=False)
    Depth = db.Column(db.Integer, nullable=False)
    PurchaseOrder = db.Column(db.String(200), nullable=False)
    Label = db.Column(db.String(20), unique=True, nullable=False)
    Sizes = db.Column(db.Integer, nullable=False)









    def __repr__(self):
        return f"Post('{self.user_id}', '{self.date_posted}')"
