from behave import given, when, then
from test.factories.user import UserFactory
from django.contrib.auth.models import User
from .users.profile import Profile
from .users.UserRoles import UserRoles

@then('I am redirected to the {webpage} page')
def step_impl(context, webpage):
    br=context.browser
    if webpage == 'home':
        assert not br.url.endswith('next=/')
    return
    redirector = {
        'messages' : '/messages/',
        'task' : '/tasks/'
    }
    assert br.url.endswith(redirector[webpage])

@given('I am an existing user who tries to access the site')
def step_impl(context):
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    # Don't omit to call save() to insert object in database
    u.save()

@given('I am mentoring that worker')
def step_impl(context):
    w = User.objects.get(username='worker')
    m = User.objects.get(username='mentor')
    p = Profile.objects.get(user_id=w.id)
    p.mentor_id = m.id
    p.save()

@given('I am logged in as the user with {role} access')
def step_impl(context, role):
    br = context.browser
    br.visit(context.base_url)
    br.fill('username', role)
    br.fill('password', 'bar')
    br.find_by_id('submit').first.click()

@given('there is one user with {role} access')
@given('I am an existing user with {role} access')
def step_impl(context, role):
    u = UserFactory(username=role)
    u.set_password('bar')
    u.save()
    p = Profile.objects.get(user_id=u.id)
    p.role = role
    p.save()

@given('I logout')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url)
    br.find_link_by_text("Logout").first.click()



