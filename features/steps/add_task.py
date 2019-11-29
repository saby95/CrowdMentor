from behave import given, when, then
from django.contrib.auth.models import User
from tasks.models import TaskUserJunction

@when('I give valid task')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/add_tasks/')

    # Fill login form and submit it (valid version)
    br.fill('task_desc', 'Task 1')
    print('give valid task: ', br.url)
    br.find_by_id('id_add_task').first.click()

@when('I try to add a task')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/add_tasks/')

    # Fill login form and submit it (valid version)

@then('I get error saying permission denied')
def step_impl(context):
    br = context.browser
    assert br.is_text_present('Permission Denied!')


@then('I can view the details of a task')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/'+str(context.task.id))
    print(br.html)
    # Fill login form and submit it (valid version)
    assert br.is_text_present('New task')
