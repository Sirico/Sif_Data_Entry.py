import os
import secrets

import datetime as datetime

import numpy as np
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, jsonify
from pip._internal.utils import datetime

from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, Entry, User
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import flask_excel as excel
import pandas as pd
import datetime

# Variables


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
def entry(df=None):
    form = Entry()

    # If entry form is submitted
    # if form.submit():
    if request.method == 'POST':
        print(form.Adult_Sizes.data)
        print(form.Kids_Sizes.data)
        # write form data to an excel file, for every size create a new row in the excel file

        # if length of form.Kids_Sizes.data and form.Adult_Sizes.data are not equal make them equal.

        if form.Kids_Sizes.data == None:
            form.Kids_Sizes.data = ['']
        if form.Adult_Sizes.data == None:
            form.Adult_Sizes.data = ['']
        if len(form.Kids_Sizes.data) != len(form.Adult_Sizes.data):
            if len(form.Kids_Sizes.data) > len(form.Adult_Sizes.data):
                for i in range(len(form.Kids_Sizes.data) - len(form.Adult_Sizes.data)):
                    if form.Kids_Sizes.data is None:
                        form.Kids_Sizes.data = ['']

                    form.Adult_Sizes.data.append('')


            else:
                for i in range(len(form.Adult_Sizes.data) - len(form.Kids_Sizes.data)):
                    if form.Adult_Sizes.data is None:
                        form.Adult_Sizes.data = ['']
                    form.Kids_Sizes.data.append('')


        df = pd.DataFrame(form.data)

        # create a variable use data from form.SKU.data
        User = current_user.username
        SKU = request.form.get('SKU')
        time = (datetime.datetime.now().strftime("%H:%M:%S"))
        date = (datetime.date.today().strftime("%d-%m-%Y"))
        exports = 'static/exports'
        xlsx = f'/home/darren/PycharmProjects/Sif/Flaskblog/flaskblog/static/Exports/SKU:{SKU} User:{User} {time} {date}.xlsx'
        csv = f'/home/darren/PycharmProjects/Sif/Flaskblog/flaskblog/static/Exports/SKU:{SKU} User:{User} {time} {date}.csv'
        form_data = [form.SKU.data, form.Parent.data, form.Brand.data, form.Gender.data, form.Closure.data,
                     form.Model.data, form.Type.data, form.Colour.data, form.Country_Manu.data, form.Upper_Mat.data,
                     form.Lining_Mat.data, form.Insole_Mat.data, form.Heel_Height.data, form.Weight.data,
                     form.Length.data, form.Depth.data, form.PurchaseOrder.data, form.Label.data, form.Kids_Sizes.data,
                     form.Adult_Sizes.data,
                     form.submit.data]

        # df = pd.DataFrame({form_data})
        # add to database
        # db.session.add(entry)
        # db.session.commit()
        # df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()),columns=form.data, index=form.data , startrow=len(df))

        # If the parent box is checked add another row to df. Remove True from df2 parent box
        if form.Parent.data == True:
            # copy the sku and the word parent into the Parent column cell
            df['Parent'] = 'Parent'+df['SKU'].map(str)
        elif form.Parent.data == False:
            df['Parent'] = ''



            # add the parent column to the df

            # df1 = pd.DataFrame(form.data)

            # df2 = pd.DataFrame(form.data)
            # df2.drop(df2.columns[1], axis=1, inplace=True)

            # add df2 to df1 as a new row
            # df = df.append(df2)

            # Copy a new row for every multicheckbox item.

        for i in range(len(form.Kids_Sizes.data)):
                # create a new row drop last two columns
                df2 = pd.DataFrame(form.data)

                df3 = pd.DataFrame(form.data)
                df3.drop(df3.columns[1], axis=1, inplace=True)

                # join the new row to the end of the dataframe
                df = df.append(df3)


        for i in range(len(form.Adult_Sizes.data)):

                # create a new row

            df4 = pd.DataFrame()



                # join the new row to the df
            df = df.append(df4)




        df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()),
                        columns=form.data, index=False)
        df.to_csv(csv, index=False)

    return render_template('entry.html', title='Entry', form=form)
