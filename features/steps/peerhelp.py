from behave import given, when, then
from peerhelp.models import Question, Answer, QuestionVotes, AnswerVotes
from django.contrib.auth.models import User

@given('I have a question which I need help with')
def step_impl(context):
    pass

@then('I can post my question')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/help/add_ques/')
    br.fill('question_summary', 'my question?')
    br.find_by_id('id_add_question').first.click()
    assert br.url.endswith('/help/')
    assert br.is_text_present('New Question Added')

@given('there exists a question')
def step_impl(context):
    u = User.objects.create(username='Joe')
    q = Question(question_summary='Does this work?', creator_id=u)
    q.save()
    context.ques = q
    context.user = u

@given('there exists a question with an answer')
def step_impl(context):
    context.execute_steps(u'given there exists a question')
    a = Answer(question=context.ques, answer_text='It sure does!',
               creator_id=context.user)
    a.save()
    context.ans = a

@then('I can answer the question')
def step_impl(context):
    br = context.browser
    br.visit(context.base_url + '/help/'+ str(context.ques.id))
    br.fill('answer_text', 'I sure hope so!')
    br.find_by_id('id_add_answer').first.click()
    assert br.is_text_present('New Answer Added')

@then('I can {voteType} the question')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/')
    assert br.is_text_present('1')

@then('I can {voteType} the answer')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/'+ str(context.ques.id)+ '/' +
            str(context.ans.id) + '/'+voteType)
    assert br.is_text_present('1')

@then('I can remove {voteType} a question')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help')
    assert br.is_text_present('0')

@then('I will {voteType} a question')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help')
    assert br.is_text_present('1')


@when('I click the {voteType} even number of times')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/'+ str(context.ques.id)+ '/'+ voteType)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' + voteType)
    print(br.html)

@when('I click the {voteType} odd number of times')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/'+ str(context.ques.id)+ '/'+ voteType)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' + voteType)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' + voteType)
    print(br.html)

@when('I click {voteType1} and then {voteType2}')
def step_impl(context, voteType1, voteType2):
    br = context.browser
    br.visit(context.base_url + '/help/'+ str(context.ques.id)+ '/'+ voteType1)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' + voteType2)





@then('I can remove {voteType} an answer')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/'+str(context.ques.id))
    assert br.is_text_present('0')

@then('I will {voteType} an answer')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/'+str(context.ques.id))
    assert br.is_text_present('1')


@when('I click the {voteType} even number of times the answer')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType)
    print(br.html)

@when('I click the {voteType} odd number of times the answer')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType)
    print(br.html)

@when('I on the answer type click {voteType1} and then {voteType2}')
def step_impl(context, voteType1, voteType2):
    br = context.browser
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType1)
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' +
             str(context.ans.id) + '/' + voteType2)


@when('I {voteType} once')
def step_impl(context, voteType):
    br = context.browser
    br.visit(context.base_url + '/help/' + str(context.ques.id) + '/' + voteType)
    print(br.html)