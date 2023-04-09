from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, ValidationError
from .models import User

class LoginForm(FlaskForm):
    username = StringField(label='NetlinkID', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    submit = SubmitField(label='Login')

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        username = User.query.filter_by(username=username_to_check.data).first()
        if username:
            raise ValidationError('User already exists! Please try a different NetlinkID')
        if '@uvic.ca' not in username:
            raise ValidationError('Not a valid NetlinkID! Please try again')

    username = StringField(label='NetlinkID', validators=[InputRequired()])
    password1 = PasswordField(label='Password', validators=[InputRequired()])
    password2 = PasswordField(label='Password', validators=[EqualTo('password1'), InputRequired()])
    submit = SubmitField(label='Register')
