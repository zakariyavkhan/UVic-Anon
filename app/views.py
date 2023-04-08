from . import db
from flask import render_template, Blueprint, request
# from .forms import *
# from .models import *

# logged in and not logged in blueprints?
home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def home_page():
    # query all posts with (now() - timestamp) < 24 hrs
    return render_template('home.html')

@home.route('/login/', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')

@home.route('/register/', methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')

@home.route('/verify/', methods=['GET', 'POST'])
def verify_page():
    return render_template('verify.html')

@home.route('/post/', methods=['GET', 'POST'])
def post_page():
    return render_template('post.html')