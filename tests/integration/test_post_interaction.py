from app.models import Comment, Vote

# TC-4
def test_post_interaction():
    comment = Comment(content='user 1 comment content', user_id=1, post_id=1)
    vote = Vote(vote_type=True, user_id=1, post_id=1)

    assert comment.content == 'user 1 comment content'
    assert comment.user_id == 1
    assert comment.post_id == 1
    assert vote
    assert vote.user_id == 1
    assert vote.post_id == 1
