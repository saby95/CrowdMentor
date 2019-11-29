from behave import given, when, then
from django.contrib.auth.models import User
from test.factories.user import UserFactory

@when('I change any user role')
def step_impl(context):
    # change the role of the worker(username = worker)
    # added in the previous step to mentor
    br = context.browser
    br.visit(context.base_url + '/change_roles/')
    u = User.objects.get(username='worker')
    id = u.id
    br.find_by_id('id_role_'+str(id)).first.select('mentor')
    br.find_by_id('id_change_role').first.click()
