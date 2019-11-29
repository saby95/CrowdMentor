from behave import given, when, then
from django.contrib.auth.models import User
from .tasks.models import ResearchTasks, TaskUserJunction

@given('there is an open task')
def step_impl(context):
    r = ResearchTasks()
    r.save()
    context.task = r

@then('I can claim the task')
def step_impl(context):
    r = ResearchTasks.objects.get(num_workers=1)
    br = context.browser
    # When worker clicks the claim button
    br.visit(context.base_url + '/tasks/' + str(r.id) + '/claim')
    # She should be redirected to the tasks page
    assert br.url.endswith('/tasks/')
    assert br.is_text_present('New Task Claimed')

@given('I have claimed a task')
def step_impl(context):
    context.execute_steps(u'given there is an open task')
    u = User.objects.get(username='worker')
    tuj = TaskUserJunction(worker_id=u, task_id=context.task)
    tuj.save()

@then('I can complete the task')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/claimed/' + str(context.task.id) +
             '/answer')
    br.fill('answer', 'my awesome answer')
    br.find_by_id('submit').first.click()
    assert br.url.endswith('/tasks/claimed/')
    assert br.is_text_present('Answer Added')

