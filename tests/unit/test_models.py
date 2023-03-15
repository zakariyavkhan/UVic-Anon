from app.models import User

def test_new_user():
    user = User('test@email.com', 'testPASSWORD')
    assert user.email == 'test@email.com'
    assert user.password == 'testPASSWORD'
    assert user.verified == False