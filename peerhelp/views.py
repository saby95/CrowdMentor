
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Question, Answer, QuestionVotes, AnswerVotes

from .forms import QuestionForm, AnswerForm

@login_required
def index(request):
    user = User.objects.get(username=request.user.username)
    questions = Question.objects.all()
    collections = []
    for question in questions:
        try:
            ques_vote = QuestionVotes.objects.get(question=question,voter_id=user)
        except QuestionVotes.DoesNotExist:
            ques_vote = None
        collection = {}
        if ques_vote:
            collection['question'] = question
            collection['upvote'] = ques_vote.up_vote
            collection['downvote'] = ques_vote.down_vote
            collection['creation_time'] = question.creation_time
        else:
            collection['question'] = question
            collection['upvote'] = False
            collection['downvote'] = False
            collection['creation_time'] = question.creation_time
        collections.append(collection)
    collections.sort(key=lambda item: item['creation_time'], reverse=True)
    context = {
            'collections': collections,
        }
    return render(request, 'questions/index.html', context)

@login_required
def add_question(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.creator_id = user
            ques.save()
            messages.info(request, 'New Question Added')
            return HttpResponseRedirect('/help/')
    else:
        form = QuestionForm()
    return render(request, 'questions/add_question.html', {'form': form})

@login_required
def detail(request,ques_id):
    user = User.objects.get(username=request.user.username)
    try:
        ques = Question.objects.get(pk=ques_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.question = ques
            ans.creator_id = user
            ans.save()
            messages.info(request, 'New Answer Added')
            return HttpResponseRedirect(request.path_info)
    else:
        answers = Answer.objects.filter(question = ques)
        try:
            ques_vote = QuestionVotes.objects.get(question=ques,voter_id=user)
        except QuestionVotes.DoesNotExist:
            ques_vote = None
        ques_up_down = {}
        if ques_vote:
            ques_up_down['upvote'] = ques_vote.up_vote
            ques_up_down['downvote'] = ques_vote.down_vote
        else:
            ques_up_down['upvote'] = False
            ques_up_down['downvote'] = False
        collections = []
        for answer in answers:
            try:
                ans_vote = AnswerVotes.objects.get(answer=answer,voter_id=user)
            except AnswerVotes.DoesNotExist:
                ans_vote = None
            collection = {}
            if ans_vote:
                collection['answer'] = answer
                collection['upvote'] = ans_vote.up_vote
                collection['downvote'] = ans_vote.down_vote
                collection['creation_time'] = answer.creation_time
            else:
                collection['answer'] = answer
                collection['upvote'] = False
                collection['downvote'] = False
                collection['creation_time'] = answer.creation_time
            collections.append(collection)
        form = AnswerForm()
        collections.sort(key=lambda item: item['creation_time'], reverse=True)
    context = {
            'ques_up_down': ques_up_down,
            'question':ques,
            'collections': collections,
            'form': form
        }
    return render(request, 'questions/detail.html', context)

@login_required
def ques_upvote(request, ques_id):
    user = User.objects.get(username=request.user.username)
    try:
        ques = Question.objects.get(pk=ques_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        vote_exist = QuestionVotes.objects.get(voter_id=user, question=ques)
    except QuestionVotes.DoesNotExist:
        vote_exist = None
    if vote_exist:
        if vote_exist.up_vote:
            vote_exist.up_vote = False
            vote_exist.save()
            ques.up_votes -= 1
            ques.save()
        else:
            if vote_exist.down_vote:
                vote_exist.down_vote = False
                vote_exist.up_vote = True
                vote_exist.save()
                ques.down_votes -= 1
                ques.up_votes += 1
                ques.save()
            else:
                vote_exist.up_vote = True
                vote_exist.save()
                ques.up_votes += 1
                ques.save()

    else:
        ques_votes = QuestionVotes()
        ques_votes.question = ques
        ques_votes.voter_id = user
        ques_votes.up_vote = True
        ques_votes.save()
        ques.up_votes += 1
        ques.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def ans_upvote(request, ques_id, ans_id):
    user = User.objects.get(username=request.user.username)
    try:
        ans = Answer.objects.get(pk=ans_id)
    except AnswerVotes.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        vote_exist = AnswerVotes.objects.get(voter_id=user, answer=ans)
    except AnswerVotes.DoesNotExist:
        vote_exist = None
    if vote_exist:
        if vote_exist.up_vote:
            vote_exist.up_vote = False
            vote_exist.save()
            ans.up_votes -= 1
            ans.save()
        else:
            if vote_exist.down_vote:
                vote_exist.down_vote = False
                vote_exist.up_vote = True
                vote_exist.save()
                ans.down_votes -= 1
                ans.up_votes += 1
                ans.save()
            else:
                vote_exist.up_vote = True
                vote_exist.save()
                ans.up_votes += 1
                ans.save()
    else:
        ans_votes = AnswerVotes()
        ans_votes.answer = ans
        ans_votes.voter_id = user
        ans_votes.up_vote = True
        ans_votes.save()
        ans.up_votes += 1
        ans.save()
    return HttpResponseRedirect('/help/'+str(ques_id)+'/')


@login_required
def ques_downvote(request, ques_id):
    user = User.objects.get(username=request.user.username)
    try:
        ques = Question.objects.get(pk=ques_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        vote_exist = QuestionVotes.objects.get(voter_id=user, question=ques)
    except QuestionVotes.DoesNotExist:
        vote_exist = None
    if vote_exist:
        if vote_exist.down_vote:
            vote_exist.down_vote = False
            vote_exist.save()
            ques.down_votes -= 1
            ques.save()
        else:
            if vote_exist.up_vote:
                vote_exist.up_vote = False
                vote_exist.down_vote = True
                vote_exist.save()
                ques.up_votes -= 1
                ques.down_votes += 1
                ques.save()
            else:
                vote_exist.down_vote = True
                vote_exist.save()
                ques.down_votes += 1
                ques.save()
    else:
        ques_votes = QuestionVotes()
        ques_votes.question = ques
        ques_votes.voter_id = user
        ques_votes.down_vote = True
        ques_votes.save()
        ques.down_votes += 1
        ques.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def ans_downvote(request, ques_id, ans_id):
    user = User.objects.get(username=request.user.username)
    try:
        ans = Answer.objects.get(pk=ans_id)
    except Answer.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        vote_exist = AnswerVotes.objects.get(voter_id=user, answer=ans)
    except AnswerVotes.DoesNotExist:
        vote_exist = None
    if vote_exist:
        if vote_exist.down_vote:
            vote_exist.down_vote = False
            vote_exist.save()
            ans.down_votes -= 1
            ans.save()
        else:
            if vote_exist.up_vote:
                vote_exist.up_vote = False
                vote_exist.down_vote = True
                vote_exist.save()
                ans.up_votes -= 1
                ans.down_votes += 1
                ans.save()
            else:
                vote_exist.down_vote = True
                vote_exist.save()
                ans.down_votes += 1
                ans.save()
    else:
        ans_votes = AnswerVotes()
        ans_votes.answer = ans
        ans_votes.voter_id = user
        ans_votes.down_vote = True
        ans_votes.save()
        ans.down_votes += 1
        ans.save()
    return HttpResponseRedirect('/help/'+str(ques_id)+'/')
