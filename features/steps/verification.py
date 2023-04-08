from behave import *

@given(u'A new user registers for UvicAnon with valid username')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given A new user registers for UvicAnon with valid username')


@when(u'The user submits registration form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user submits registration form')


@then(u'A verification email is sent to the netlinkid')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A verification email is sent to the netlinkid')


@given(u'A new user registers for UvicAnon with invalid username')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given A new user registers for UvicAnon with invalid username')


@then(u'The username fails form validation')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The username fails form validation')