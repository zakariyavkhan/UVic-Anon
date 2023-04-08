from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('NetlinkID', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    # add regex validator to NetlinkID
    username = StringField('NetlinkID', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')