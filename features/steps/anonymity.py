from behave import given, when, then
from flask_login import current_user

# create valid user
@given(u'A user is logged in')
def step_impl(context):
    # log user in
    pass

@when(u'The user visits the home page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000')

@then(u'No usernames will be visible')
def step_impl(context):
    assert '@uvic.ca' not in context.browser.page_source