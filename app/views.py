from . import db
from flask import render_template, Blueprint, request
# from .forms import *
# from .models import *

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

login = Blueprint('login', __name__)

@login.route('/login/', methods=['GET', 'POST'])
def index():
    return render_template('login.html')

register = Blueprint('register', __name__)

@register.route('/register/', methods=['GET', 'POST'])
def index():
    return render_template('register.html')