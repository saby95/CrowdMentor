
from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    question_summary = models.CharField(max_length=200, default = 'Add question summary')
    question_desc = models.TextField(default = 'Add question description')
    creation_time = models.DateTimeField(auto_now_add=True)
    creator_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question_summary

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    creator_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.answer_text

class QuestionVotes(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voter_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    up_vote = models.BooleanField(default=False)
    down_vote = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question_summary

class AnswerVotes(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    voter_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    up_vote = models.BooleanField(default=False)
    down_vote = models.BooleanField(default=False)

    def __str__(self):
        return self.answer.answer_text
