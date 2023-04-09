from behave import *

@given(u'A new user wants to register for UvicAnon with valid username')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/register')
    context.browser.find_element_by_name('username').send_keys('valid@uvic.ca')
    context.browser.find_element_by_name('password').send_keys('password')

@when(u'The user submits registration form')
def step_impl(context):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='Submit']").click()

@then(u'The user is routed to the verification page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/verification' 

@given(u'A new user wants to register for UvicAnon with invalid username')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/register')
    context.browser.find_element_by_name('username').send_keys('invalid@email.com')
    context.browser.find_element_by_name('password').send_keys('password')

@then(u'The username fails form validation')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/register'
    assert 'Not a valid NetlinkID! Please try again' in context.browser.page_source