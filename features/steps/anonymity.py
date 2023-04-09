from behave import given, when, then

@given(u'A user is logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given A user is logged in')


@when(u'The user visits the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user visits the home page')


@then(u'No usernames will be visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then No usernames will be visible')