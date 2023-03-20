from app.models import User

def test_user_creation():
    '''
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password variables are defined correctly
    '''
    new_user = User(email="test-email@gmail.com", password="abc123")
    assert new_user.email == "test-email@gmail.com"
    assert new_user.password == "abc123"

def test_post_creation():
    '''
    GIVEN a Post model
    WHEN a new Post is created
    THEN check the content is defined correctly
    '''
    post = Post(content='post content')
    assert post.content == 'post content'
