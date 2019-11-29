from behave import given, then, when
from django.contrib.auth.models import User
from .users.profile import Profile
from .tasks.models import ResearchTasks, TaskUserJunction

@given('there is a worker')
def step_impl(context):
    u = User(username='worker')
    u.save()
    context.worker = u

@given('the worker is assigned a task')
def step_impl(context):
    t = ResearchTasks(task_summary='New task', audit_prob=1, audit_by=1)
    t.save()
    context.task = t
    tuj = TaskUserJunction(task_id=t, worker_id=context.worker)
    tuj.save()

@given('I am mentoring the worker')
def step_impl(context):
    u = User.objects.get(username='worker')
    p = Profile.objects.get(user=u)
    m = User.objects.get(username='mentor')
    p.mentor = m
    p.save()
    context.mentor = m

@then('I can view the status of the worker\'s task')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/task_status/' + str(context.mentor.id)
             + '/')
    assert br.is_text_present('Task summary')

@then('other details about the task')
def step_impl(context):
    br = context.browser
    u = User.objects.get(username='worker')
    br.visit(context.base_url + '/tasks/view_task/' + str(u.id) + '/' + str(context.task.id) + '/')
    print (br.html)
    assert br.is_text_present('Task Description')

@then('I can view the task status of all tasks')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/all_task_status/')
    assert br.is_text_present('Mentor')
