from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, \
    IntegerField, SelectMultipleField, DateField, validators, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import flaskblog
from flaskblog import choices
from flaskblog.models import User
from datetime import datetime
from wtforms import widgets


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


#
# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
#     option_widget = widgets.CheckboxInput()
# create a multi-checkbox field for multiple sizes

# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
#     option_widget = widgets.CheckboxInput()
#     # override the default get_label method to add the '$' symbol
#     def get_label(self, option):
#         return '%s' % option


# create a multi-checkbox field for multiple sizes that keeps all arrays in the same length.
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

    # override the default get_label method to add the '$' symbol
    def get_label(self, option):
        return '%s' % option


date = datetime.now()


# Entry Form with a button for Adults and a button for Kids
class Entry(FlaskForm):
    Adults = SubmitField('Adults')
    Kids = SubmitField('Kids')


class Adults(FlaskForm):
    Footwear = SubmitField('Footwear')
    Clothing = SubmitField('Clothing')
    Accessories = SubmitField('Accessories')


class Kids(FlaskForm):
    Kids_Footwear = RadioField('Kids_Footwear', choices=choices.Kids_Footwear)
    Kids_Clothing = RadioField('Kids_Clothing', choices=choices.Kids_Clothing)



# Entry form content
class Adults_Footwear(FlaskForm):
    User = current_user
    Date = date.strftime("%a"' ' "%b" ' ' '%d' ' ' '%Y')
    Time = date.strftime("%R")
    SKU = StringField("SKU", validators=[DataRequired()])
    Parent = BooleanField('Is this a parent SKU?', default='unchecked')
    # create an author field using current_user.id
    Author = StringField("Author", validators=[DataRequired()])

    # Brand with choices from choices.py

    Brand = SelectField("Brand", choices=choices.Brand, validators=[DataRequired()])
    Gender = SelectField("Select Gender", choices=['', 'Female', 'Male', 'Kids'])
    Closure = SelectField("Select Closure Type", choices=['', 'test'], validators=[DataRequired()])
    Model = StringField("Select Model", validators=[DataRequired()])
    Type = SelectField("Select Type", choices=choices.Type_Footwear, validators=[DataRequired()])
    Colour = SelectField("Select main colour", choices=choices.Colour, validators=[DataRequired()])
    Country_Manu = SelectField("Select the country of manufacture", choices=choices.Country,
                               validators=[DataRequired()])
    Upper_Mat = SelectField("Select the upper material", choices=['', 'Leather'], validators=[DataRequired()])
    Lining_Mat = SelectField("Select the lining material", choices=['', 'test'], validators=[DataRequired()])
    Insole_Mat = SelectField("Select the insole material", choices=['', 'test'], validators=[DataRequired()])
    Heel_Height = IntegerField("Input the heel height in cm", validators=[DataRequired()])
    Weight = IntegerField("Input the weight in KG", validators=[DataRequired()])
    Height = IntegerField("Input the products height in cm", validators=[DataRequired()])
    Length = IntegerField("Input the products length in cm", validators=[DataRequired()])
    Depth = IntegerField("Input the products depth in cm", validators=[DataRequired()])
    PurchaseOrder = StringField("Input the purchase order number", validators=[DataRequired()])
    Label = SelectField("Select the label", choices=['', 'test'], validators=[DataRequired()])
    Sizes = MultiCheckboxField("Select the sizes", choices=choices.Adults_Footwear)

    Finalise = BooleanField('Finalise')

    submit = SubmitField('Submit')



# Entry form content
class Kids_Footwear(FlaskForm):
    User = current_user
    Date = date.strftime("%a"' ' "%b" ' ' '%d' ' ' '%Y')
    Time = date.strftime("%R")
    SKU = StringField("SKU", validators=[DataRequired()])
    Parent = BooleanField('Is this a parent SKU?', default='unchecked')
    # create an author field using current_user.id
    Author = StringField("Author", validators=[DataRequired()])

    # Brand with choices from choices.py

    Brand = SelectField("Brand", choices=choices.Brand, validators=[DataRequired()])
    Gender = SelectField("Select Gender", choices=['', 'Female', 'Male', 'Kids'])
    Closure = SelectField("Select Closure Type", choices=['', 'test'], validators=[DataRequired()])
    Model = StringField("Select Model", validators=[DataRequired()])
    Type = SelectField("Select Type", choices=choices.Type_Footwear, validators=[DataRequired()])
    Colour = SelectField("Select main colour", choices=choices.Colour, validators=[DataRequired()])
    Country_Manu = SelectField("Select the country of manufacture", choices=choices.Country,
                               validators=[DataRequired()])
    Upper_Mat = SelectField("Select the upper material", choices=['', 'Leather'], validators=[DataRequired()])
    Lining_Mat = SelectField("Select the lining material", choices=['', 'test'], validators=[DataRequired()])
    Insole_Mat = SelectField("Select the insole material", choices=['', 'test'], validators=[DataRequired()])
    Heel_Height = IntegerField("Input the heel height in cm", validators=[DataRequired()])
    Weight = IntegerField("Input the weight in KG", validators=[DataRequired()])
    Height = IntegerField("Input the products height in cm", validators=[DataRequired()])
    Length = IntegerField("Input the products length in cm", validators=[DataRequired()])
    Depth = IntegerField("Input the products depth in cm", validators=[DataRequired()])
    PurchaseOrder = StringField("Input the purchase order number", validators=[DataRequired()])
    Label = SelectField("Select the label", choices=['', 'test'], validators=[DataRequired()])
    Sizes = MultiCheckboxField("Select the sizes", choices=choices.Kids_Footwear)

    Finalise = BooleanField('Finalise')

    submit = SubmitField('Submit')
    # create a button to finish the form


class Kids_Clothing(FlaskForm):
    User = current_user
    Date = date.strftime("%a"' ' "%b" ' ' '%d' ' ' '%Y')
    Time = date.strftime("%R")
    SKU = StringField("SKU", validators=[DataRequired()])
    Parent = BooleanField('Is this a parent SKU?', default='unchecked')
    # create an author field using current_user.id
    Author = StringField("Author", validators=[DataRequired()])

    # Brand with choices from choices.py

    Brand = SelectField("Brand", choices=choices.Brand, validators=[DataRequired()])
    Gender = SelectField("Select Gender", choices=['', 'Female', 'Male', 'Kids'])
    Closure = SelectField("Select Closure Type", choices=choices.Type_Clothing, validators=[DataRequired()])
    Model = StringField("Select Model", validators=[DataRequired()])
    Type = SelectField("Select Type", choices=choices.Type_Clothing, validators=[DataRequired()])
    Colour = SelectField("Select main colour", choices=choices.Colour, validators=[DataRequired()])
    Country_Manu = SelectField("Select the country of manufacture", choices=choices.Country,
                               validators=[DataRequired()])
    Upper_Mat = SelectField("Select the upper material", choices=['', 'Leather'], validators=[DataRequired()])
    Lining_Mat = SelectField("Select the lining material", choices=['', 'test'], validators=[DataRequired()])
    Insole_Mat = SelectField("Select the insole material", choices=['', 'test'], validators=[DataRequired()])
    Heel_Height = IntegerField("Input the heel height in cm", validators=[DataRequired()])
    Weight = IntegerField("Input the weight in KG", validators=[DataRequired()])
    Height = IntegerField("Input the products height in cm", validators=[DataRequired()])
    Length = IntegerField("Input the products length in cm", validators=[DataRequired()])
    Depth = IntegerField("Input the products depth in cm", validators=[DataRequired()])
    PurchaseOrder = StringField("Input the purchase order number", validators=[DataRequired()])
    Label = SelectField("Select the label", choices=['', 'test'], validators=[DataRequired()])
    Sizes = MultiCheckboxField("Select the sizes", choices=choices.Kids_Clothing)

    Finalise = BooleanField('Finalise')

    submit = SubmitField('Submit')


class Adults_Clothing(FlaskForm):
    User = current_user
    Date = date.strftime("%a"' ' "%b" ' ' '%d' ' ' '%Y')
    Time = date.strftime("%R")
    SKU = StringField("SKU", validators=[DataRequired()])
    Parent = BooleanField('Is this a parent SKU?', default='unchecked')
    # create an author field using current_user.id
    Author = StringField("Author", validators=[DataRequired()])

    # Brand with choices from choices.py

    Brand = SelectField("Brand", choices=choices.Brand, validators=[DataRequired()])
    Gender = SelectField("Select Gender", choices=['', 'Female', 'Male', 'Kids'])
    Closure = SelectField("Select Closure Type", choices=choices.Type_Closure, validators=[DataRequired()])
    Model = StringField("Select Model", validators=[DataRequired()])
    Type = SelectField("Select Type", choices=choices.Type_Clothing, validators=[DataRequired()])
    Colour = SelectField("Select main colour", choices=choices.Colour, validators=[DataRequired()])
    Country_Manu = SelectField("Select the country of manufacture", choices=choices.Country,
                               validators=[DataRequired()])
    Upper_Mat = SelectField("Select the upper material", choices=['', 'Leather'], validators=[DataRequired()])
    Lining_Mat = SelectField("Select the lining material", choices=['', 'test'], validators=[DataRequired()])
    Insole_Mat = SelectField("Select the insole material", choices=['', 'test'], validators=[DataRequired()])
    Heel_Height = IntegerField("Input the heel height in cm", validators=[DataRequired()])
    Weight = IntegerField("Input the weight in KG", validators=[DataRequired()])
    Height = IntegerField("Input the products height in cm", validators=[DataRequired()])
    Length = IntegerField("Input the products length in cm", validators=[DataRequired()])
    Depth = IntegerField("Input the products depth in cm", validators=[DataRequired()])
    PurchaseOrder = StringField("Input the purchase order number", validators=[DataRequired()])
    Label = SelectField("Select the label", choices=['', 'test'], validators=[DataRequired()])
    Sizes = MultiCheckboxField("Select the sizes", choices=choices.Adults_Clothing)

    Finalise = BooleanField('Finalise')

    submit = SubmitField('Submit')

class Accessories(FlaskForm):
    User = current_user
    Date = date.strftime("%a"' ' "%b" ' ' '%d' ' ' '%Y')
    Time = date.strftime("%R")
    SKU = StringField("SKU", validators=[DataRequired()])
    Parent = BooleanField('Is this a parent SKU?', default='unchecked')
    # create an author field using current_user.id
    Author = StringField("Author", validators=[DataRequired()])

    # Brand with choices from choices.py

    Brand = SelectField("Brand", choices=choices.Brand, validators=[DataRequired()])
    Gender = SelectField("Select Gender", choices=['', 'Female', 'Male', 'Kids'])
    Closure = SelectField("Select Closure Type", choices=choices.Type_Closure, validators=[DataRequired()])
    Model = StringField("Select Model", validators=[DataRequired()])
    Type = SelectField("Select Type", choices=choices.Type_Accessories, validators=[DataRequired()])
    Colour = SelectField("Select main colour", choices=choices.Colour, validators=[DataRequired()])
    Country_Manu = SelectField("Select the country of manufacture", choices=choices.Country,
                               validators=[DataRequired()])
    Upper_Mat = SelectField("Select the upper material", choices=['', 'Leather'], validators=[DataRequired()])
    Lining_Mat = SelectField("Select the lining material", choices=['', 'test'], validators=[DataRequired()])
    Insole_Mat = SelectField("Select the insole material", choices=['', 'test'], validators=[DataRequired()])
    Heel_Height = IntegerField("Input the heel height in cm", validators=[DataRequired()])
    Weight = IntegerField("Input the weight in KG", validators=[DataRequired()])
    Height = IntegerField("Input the products height in cm", validators=[DataRequired()])
    Length = IntegerField("Input the products length in cm", validators=[DataRequired()])
    Depth = IntegerField("Input the products depth in cm", validators=[DataRequired()])
    PurchaseOrder = StringField("Input the purchase order number", validators=[DataRequired()])
    Label = SelectField("Select the label", choices=['', 'test'], validators=[DataRequired()])
    Sizes = MultiCheckboxField("Select the sizes", choices=choices.Accessories_sizes)

    Finalise = BooleanField('Finalise')

    submit = SubmitField('Submit')




