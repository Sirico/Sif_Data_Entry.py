import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, jsonify
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, Entry
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import flask_excel as excel
import pandas as pd

posts = [
    'Welcome'
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# Entry form
@app.route('/entry', methods=['GET', 'POST'])
@login_required
def entry():
    form = Entry()

    if form.validate_on_submit():
        post = Post(SKU=form.SKU.data,
                    Parent=form.Parent.data,
                    Brand=form.Brand.data,
                    Gender=form.Gender.data,
                    Closure=form.Closure.data,
                    Model=form.Model.data,
                    Type=form.Type.data,
                    Colour=form.Colour.data,
                    Country_Manu=form.Country_Manu.data,
                    Upper_Mat=form.Upper_Mat.data,
                    Lining_Mat=form.Lining_Mat.data,
                    Insole_Mat=form.Insole_Mat.data,
                    Heel_Height=form.Heel_Height.data,
                    Weight=form.Weight.data,
                    Height=form.Height.data,
                    Length=form.Length.data,
                    Depth=form.Depth.data,
                    Purchased_Ord=form.Purchase_Ord.data,
                    Label=form.Label.data,
                    Kids_Sizes=form.Kids_Sizes.data,
                    Adult_Sizes=form.Adult_Sizes.data, )

        db.session.commit()
        db.session.add()
    flash('Your post has been created!', 'success')

    return render_template('entry.html', title='Entry', form=form)
