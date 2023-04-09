from behave import given, when, then

@given(u'A user is logged in')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/register')
    context.browser.find_element('name', 'username').send_keys('test@uvic.ca')
    context.browser.find_element('name', 'password1').send_keys('password')
    context.browser.find_element('name', 'password2').send_keys('password')
    context.browser.find_element('xpath', f"//*[@id='submit']").click()

    context.browser.get('http://127.0.0.1:5000/login')
    context.browser.find_element('name', 'username').send_keys('test@uvic.ca')
    context.browser.find_element('name', 'password').send_keys('password')
    context.browser.find_element('xpath', f"//*[@id='submit']").click()

@when(u'The user visits the home page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000')

@then(u'No usernames will be visible')
def step_impl(context):
    assert '@uvic.ca' not in context.browser.page_source