import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    app.config['SECRET_KEY']='dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'database.db')    
    db.init_app(app)

    from .models import User, Post, Comment
    with app.app_context():
        db.create_all()

    # with app.app_context():
    #     db.session.add(Node(name=line[0], id=line[1]))
    #     db.session.commit()

    return app
