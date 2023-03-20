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
