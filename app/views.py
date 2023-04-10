from . import db
from flask import render_template, Blueprint, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from .models import User, Post
from sqlalchemy.sql import select
from flask_login import login_user

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def home_page():
    posts = db.session.scalars(select(Post).where(Post.expired == False)).all()
    return render_template('home.html', posts=posts)

@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        attempted_user = db.session.scalars(select(User).where(User.username == form.username.data)).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are now logged in', category='success')
            return redirect(url_for('home.home_page'))
        
        else:
            flash('There was an error logging in', category='danger')
    
    # if request.method == 'POST' and form.errors != {}:
    #     for err_msg in form.errors.values():
    #         flash(f'There was an error logging in: {err_msg}', category='danger')

    return render_template('login.html', form=form)

@home.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home.verify_page'))
    
    if request.method == 'POST' and form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@home.route('/verify', methods=['GET', 'POST'])
def verify_page():
    # login_user(user_to_create)
    return render_template('verify.html')

@home.route('/post', methods=['GET', 'POST'])
def post_page():
    return render_template('post.html')