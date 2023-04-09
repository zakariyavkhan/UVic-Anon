import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__, static_folder="templates/static")
    app.config['SECRET_KEY']='dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'database.db')    
    
    from .models import User, Post, Comment, Vote
    with app.app_context():
        db.init_app(app)
        db.create_all()

    from .views import home
    app.register_blueprint(home)

    return app
