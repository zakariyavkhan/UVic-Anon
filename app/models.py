from app import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='user', lazy=True) # 1 to many relationship
    comments = db.relationship('Comment', backref='user', lazy=True) # 1 to many relationship

    def __repr__(self):
        return 'User {}'.format(self.email)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime(timezone=True), unique=False, default=func.now())
    # date = db.Column(db.DateTime, unique=False, nullable=False)
    expired = db.Column(db.Boolean, nullable=False)
    upvotes = db.Column(db.Integer, nullable=False, default=0)
    downvotes = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(db.String(120), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True) # 1 to many relationship
    
    def __repr__(self):
        return 'Post ID {}'.format(self.id)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.DateTime, unique=False, nullable=False)
    # upvotes = db.Column(db.Integer, nullable=False)
    # downvotes = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return 'Comment ID {}'.format(self.id)
  
