from app import db
from sqlalchemy import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'User {self.email}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime(timezone=True), unique=False, default=func.now())
    expired = db.Column(db.Boolean, nullable=False, default=False)
    content = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'Post ID {self.id}'
