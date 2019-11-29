from tasks.models import ResearchTasks, Audit, TaskUserJunction
from django.contrib.auth.models import User
from test.factories.user import UserFactory
from users.profile import Profile

@given('A task has been submitted')
def step_impl(context):
    r = ResearchTasks.objects.create(task_desc="New task",task_summary="New task to do",audit_prob=1, audit_by=1
                                     ,num_workers=1)
    context.task = r

@given('there is a task to be audited')
def step_impl(context):
    context.execute_steps(
        u'''given A task has been submitted
        given I am an existing user with worker access
        given I am logged in as the user with worker access
        ''')
    # Task gets added to the tuj when the worker claims it.
    u = User.objects.get(username='worker')
    tuj = TaskUserJunction.objects.create(worker_id=u, task_id=context.task)
    # Worker must visit the url to answer the question
    br = context.browser
    br.visit(context.base_url + '/tasks/claimed/' + str(context.task.id) +
             '/answer')
    br.fill('answer', 'my awesome answer')
    br.find_by_id('submit').first.click()
    context.execute_steps(u'given I logout')

@then('I can claim the task for audit')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/audits/' + str(context.task.id) + '/claim_audit/')
    assert br.url.endswith('/tasks/audits/')
    assert br.is_text_present('Task Claimed for Review')

@then('I can audit the task')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/audits/' + str(context.task.id) + '/submit_audit')
    br.find_by_id('id_task_correct').first.select('True')
    br.find_by_id('submit').first.click()
    assert br.url.endswith('/tasks/audits/')
    assert br.is_text_present('Review Submitted')

@then('I can view the open audits')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/open_audits/')
    assert br.is_text_present('New task')

@then('I can view the details of that audit')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/tasks/open_audits/'+str(context.task.id))
    assert br.is_text_present('New task')