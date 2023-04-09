from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, ValidationError, Email
from .models import User
from sqlalchemy.sql import select
from . import db

class LoginForm(FlaskForm):
    username = StringField(label='NetlinkID', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    submit = SubmitField(label='Login')

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user_to_check = db.session.scalars(select(User).where(User.username == username_to_check.data))
        if user_to_check:
            raise ValidationError('User already exists! Please try a different NetlinkID')
        if '@uvic.ca' not in username_to_check.data:
            raise ValidationError('Not a valid NetlinkID! Please try again')

    username = StringField(label='NetlinkID', validators=[InputRequired()])
    password1 = PasswordField(label='Password', validators=[InputRequired()])
    password2 = PasswordField(label='Password', validators=[EqualTo('password1')])
    submit = SubmitField(label='Register')
