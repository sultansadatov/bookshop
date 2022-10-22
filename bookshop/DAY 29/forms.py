from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    full_name = StringField(label="Your name", validators=[DataRequired(), Length(min=3, max=30)])
    message = TextAreaField(label="Message", validators=[DataRequired(), Length(max=255)])

class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label="Email", validators=[DataRequired(), Email(), Length(max=50)])
    password = StringField(label="Password", validators=[DataRequired(), Length(min=8, max=30)])

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField(label="Password", validators=[DataRequired(), Length(min=8, max=30)])