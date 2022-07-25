import os
import secrets

import datetime as datetime
import shutil

import numpy as np
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, jsonify
from flask_wtf import form
from pip._internal.utils import datetime

from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, Adults, Kids, Adults_Footwear, Kids_Footwear
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import os
import flask_excel as excel
import pandas as pd
import datetime
from flaskblog import choices
from flaskblog import forms

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


# Entry form to select between kids and adults
@app.route('/entry', methods=['GET', 'POST'])
@login_required
def entry(df=None):
    form = entry

    return render_template('entry.html', title='Entry', form=form)


# Adult entry form with a button for adults_footwear and adults_clothing

@app.route('/adults', methods=['GET', 'POST'])
@login_required
def adults(df=None):
    return render_template('adults.html', posts=posts)







# Kids entry form with a button for kidsfootwear and kids_clothing
@app.route('/kids', methods=['GET', 'POST'])
@login_required
def kids(df=None):
    return render_template('kids.html', posts=posts)


# Adults shoe sizes
@app.route('/adults-footwear', methods=['GET', 'POST'])
@login_required
def adults_footwear():
    form = Adults_Footwear()
    if request.method == 'POST':
        # write form data to an excel file, for every size create a new row in the excel file

        df = pd.DataFrame(form.data)

        # create a variable use data from form.SKU.data
        User = current_user.username
        SKU = request.form.get('SKU')
        time = (datetime.datetime.now().strftime("%H:%M:%S"))
        date = (datetime.date.today().strftime("%d-%m-%Y"))
        Author = current_user.username
        exports = 'static/exports'
        xlsx = f'/home/darren/PycharmProjects/Sif/Flaskblog/flaskblog/static/Exports/SKU:{SKU} User:{User} {time} {date}.xlsx'
        csv = f'/home/darren/PycharmProjects/Sif/Flaskblog/flaskblog/static/Exports/SKU:{SKU} User:{User} {time} {date}.csv'
        form_data = [form.SKU.data, form.Parent.data, form.Brand.data, form.Gender.data, form.Closure.data,
                     form.Model.data, form.Type.data, form.Colour.data, form.Country_Manu.data, form.Upper_Mat.data,
                     form.Lining_Mat.data, form.Insole_Mat.data, form.Heel_Height.data, form.Weight.data,
                     form.Length.data, form.Depth.data, form.PurchaseOrder.data, form.Label.data,
                     form.Sizes.data,
                     form.submit.data]

        df_1str = df.iloc[0]

        # Add current user to the Author column
        df['Author'] = current_user.username

        # If the parent box is checked add another row to df. Remove True from df2 parent box
        if form.Parent.data == True:
            # copy the sku and the word parent into the first row Parent column cell.
            df1 = df.copy()
            df1['Parent'] = 'Parent'

            # delete the sizes column of df1
            del df1['Sizes']

            # remove every row except the first row

            df1 = df1.iloc[0:1]

            # create df2 as the rest of the dataframe
            df2 = df.iloc[0:]
            # blank the parent column in df2
            df2['Parent'] = form.SKU.data

            # if there's more than one row in df add SKU and size to the next rows

            for i in range(0, len(df2)):
                df2.loc[i, 'SKU'] = df2.loc[i, 'SKU'] + '_' + form.Sizes.data[i]
            # concatenate df1 and df2
            df = pd.concat([df1, df2])

            df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()), index=False)
            df.to_csv(csv, index=False)


        # # if the parent is not checked then leave it blank
        elif form.Parent.data == False:
            df['Parent'] = ''

            # remove last two columns from df
            df.drop(df.columns[-2:], axis=1, inplace=True)
            df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()), index=False)
            df.to_csv(csv, index=False)

    return render_template('Adults-Footwear.html', title='Adults Footwear', form=form)


# Kids shoe sizes
@app.route('/kids_footwear', methods=['GET', 'POST'])
@login_required
def kids_footwear():
    form = Kids_Footwear()
    if request.method == 'POST':
        # write form data to an excel file, for every size create a new row in the excel file

        df = pd.DataFrame(form.data)

        # create a variable use data from form.SKU.data
        User = current_user.username
        SKU = request.form.get('SKU')
        time = (datetime.datetime.now().strftime("%H:%M:%S"))
        date = (datetime.date.today().strftime("%d-%m-%Y"))
        Author = current_user.username

        User = current_user.username
        date = (datetime.date.today().strftime("%d-%m-%Y"))
        directory = f'{form.PurchaseOrder.data}:{date}'
        parent_dir = '/home/darren/PycharmProjects/Sif/Flaskblog/flaskblog/static/Exports'
        path = os.path.join(parent_dir, directory)
        try:
            os.mkdir(path, 0o777)
        except OSError:
            pass

        xlsx = f'SKU:{SKU} User:{User} {time} {date}.xlsx'
        csv = f'SKU:{SKU} User:{User} {time} {date}.csv'
        form_data = [form.SKU.data, form.Parent.data, form.Brand.data, form.Gender.data, form.Closure.data,
                     form.Model.data, form.Type.data, form.Colour.data, form.Country_Manu.data, form.Upper_Mat.data,
                     form.Lining_Mat.data, form.Insole_Mat.data, form.Heel_Height.data, form.Weight.data,
                     form.Length.data, form.Depth.data, form.PurchaseOrder.data, form.Label.data,
                     form.Sizes.data,
                     form.submit.data]

        df_1str = df.iloc[0]

        # Add current user to the Author column
        df['Author'] = current_user.username

        # If the parent box is checked add another row to df. Remove True from df2 parent box
        if form.Parent.data == True:
            # copy the sku and the word parent into the first row Parent column cell.
            df1 = df.copy()
            df1['Parent'] = 'Parent'

            # delete the sizes column of df1
            del df1['Sizes']

            # remove every row except the first row

            df1 = df1.iloc[0:1]

            # create df2 as the rest of the dataframe
            df2 = df.iloc[0:]
            # blank the parent column in df2
            df2['Parent'] = form.SKU.data

            # if there's more than one row in df add SKU and size to the next rows

            for i in range(0, len(df2)):
                df2.loc[i, 'SKU'] = df2.loc[i, 'SKU'] + '_' + form.Sizes.data[i]
            # concatenate df1 and df2
            df = pd.concat([df1, df2])



            df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()), index=False)
            df.to_csv(csv, index=False)
            # move the files to path
            shutil.move(xlsx, path)
            shutil.move(csv, path)



        # # if the parent is not checked then leave it blank
        elif form.Parent.data == False:
            df['Parent'] = ''

            # remove last two columns from df

            df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()), index=False)
            df.to_csv(csv, index=False)
            shutil.move(xlsx, path)
            shutil.move(csv, path)

            # df = df.reindex(df.index[1:,1:])

        # write the data to files

        # df.to_excel(xlsx, sheet_name=current_user.username + '_' + str(datetime.date.today()), index=False)
        # df.to_csv(csv, index=False)

    return render_template('Kids_Footwear.html', title='Kids Footwear', form=form)
