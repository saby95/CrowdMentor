
from django.contrib import admin

from .models import Question, Answer, AnswerVotes, QuestionVotes

admin.site.register(Question)
admin.site.register(QuestionVotes)
admin.site.register(Answer)
admin.site.register(AnswerVotes)
