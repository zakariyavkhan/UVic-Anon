from . import db
from flask import render_template, Blueprint, request, redirect, url_for
from .forms import LoginForm, RegisterForm
# from .models import *

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def home_page():
    # posts = query all posts with (now() - timestamp) < 24 hrs
    # pass as parameter to home.html
    return render_template('home.html')

@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # handle login logic here
        return redirect(url_for('home.home_page'))
    return render_template('login.html', form=form)

@home.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # handle registration logic here
        return redirect(url_for('home.verify_page'))
    return render_template('register.html', form=form)

@home.route('/verify', methods=['GET', 'POST'])
def verify_page():
    return render_template('verify.html')

@home.route('/post', methods=['GET', 'POST'])
def post_page():
    return render_template('post.html')