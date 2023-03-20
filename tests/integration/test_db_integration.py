from app import create_app, db
from app.models import User, Post, Comment

app = create_app()

def test_db():
    with app.app_context():
        db.session.add(user)
        db.session.commit()

        assert db.session.execute(db.select(User)).scalar().email == 'username@email.com'
        assert db.session.execute(db.select(User)).scalar().password == 'abc123'


    with app.app_context():
        db.session.add(post)
        db.session.commit()

        assert db.session.execute(db.select(Post)).scalar().user_id == 1
        assert db.session.execute(db.select(Post)).scalar().content == 'user 1 post content'


    with app.app_context():
        db.session.add(comment)
        db.session.commit()

        assert db.session.execute(db.select(Comment)).scalar().user_id == 1
        assert db.session.execute(db.select(Comment)).scalar().post_id == 1
        assert db.session.execute(db.select(Comment)).scalar().content == 'user 1 comment content'
        assert db.session.execute(db.select(Post)).scalar().comments
