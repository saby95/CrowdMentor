from behave import given, when, then
from django.contrib.auth.models import User
from .users.profile import Profile
from .privatemessages.models import Thread

@when('I send a message to worker')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/messages/')
    br.fill('message', 'Hello Worker')
    br.find_by_id('submit').first.click()

@when('I send a message to mentor')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/messages/')
    br.fill('message', 'Hello Mentor')
    br.find_by_id('submit').first.click()

@when('I send an empty message to worker')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/messages/')
    br.find_by_id('submit').first.click()

@when('the mentor sends a message to the worker')
def step_impl(context):
    context.execute_steps(
        u'''when I send a message to worker
        given I logout'''
    )

@then('I get error saying No message found')
def step_impl(context):
    br = context.browser
    assert br.is_text_present('No message found.')

@when('the worker sends a message to the mentor')
def step_impl(context):
    context.execute_steps(
        u'''when I send a message to mentor
        given I logout'''
    )


@then('the worker is able to read the message')
def step_impl(context):
    context.execute_steps(
        u'given I am logged in as the user with worker access')
    br = context.browser
    u = User.objects.get(username='worker')
    t = Thread.objects.get(participants=u)
    br.visit(context.base_url + '/messages/chat/' + str(t.id))
    assert br.is_text_present('Hello Worker')

@then('the mentor is able to read the message')
def step_impl(context):
    context.execute_steps(
        u'given I am logged in as the user with mentor access')
    br = context.browser
    u = User.objects.get(username='mentor')
    t = Thread.objects.get(participants=u)
    br.visit(context.base_url + '/messages/chat/' + str(t.id))
    assert br.is_text_present('Hello Mentor')

