from app import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='user', lazy=True) # 1 to many relationship
    comments = db.relationship('Comment', backref='user', lazy=True) # 1 to many relationship
    votes = db.relationship('Vote', backref='user', lazy=True)

    def __repr__(self):
        return 'User {}'.format(self.email)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime(timezone=True), unique=False, default=func.now())
    expired = db.Column(db.Boolean, nullable=False, default=False)
    content = db.Column(db.String, nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True) # 1 to many relationship
    votes = db.relationship('Vote', backref='post', lazy=True)
    
    def __repr__(self):
        return 'Post ID {}'.format(self.id)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return 'Comment ID {}'.format(self.id)
    
class Vote(db.Model):
    vote_type = db.Column(db.Boolean, nullable=False) # True = upvote, False = downvote
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    
    def __repr__(self):
        if self.vote_type:
            return f'(upvote, user_id:{self.user_id}, post_id:{self.post_id})'
        else:
            return f'(downvote, user_id:{self.user_id}, post_id:{self.post_id})'
  
