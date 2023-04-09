from behave import given, when, then

@given(u'A new user wants to register for UvicAnon with valid username')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/register')
    context.browser.find_element('name', 'username').send_keys('valid@uvic.ca')
    context.browser.find_element('name', 'password1').send_keys('password')
    context.browser.find_element('name', 'password2').send_keys('password')

@when(u'The user submits registration form')
def step_impl(context):
    context.browser.find_element('xpath', f"//*[@id='submit']").click()

@then(u'The user is routed to the verification page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/verify'

@given(u'A new user wants to register for UvicAnon with invalid username')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/register')
    context.browser.find_element('name', 'username').send_keys('invalid@email.com')
    context.browser.find_element('name', 'password1').send_keys('password')
    context.browser.find_element('name', 'password2').send_keys('password')

@then(u'The username not a NetlinkID')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/register'
    assert 'Not a valid NetlinkID! Please try again' in context.browser.page_source

@given(u'A user tries to register with in use NetlinkID')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/register')
    context.browser.find_element('name', 'username').send_keys('valid@uvic.ca')
    context.browser.find_element('name', 'password1').send_keys('password')
    context.browser.find_element('name', 'password2').send_keys('password')

@then(u'The username already associated with user')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/register'
    assert 'User already exists!' in context.browser.page_source