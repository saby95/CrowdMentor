from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_question/', views.add_question, name='add_question'),
    path('<ques_id>/', views.detail, name='detail'),
    path('<ques_id>/upvote', views.ques_upvote, name='ques_upvote'),
    path('<ques_id>/<ans_id>/upvote', views.ans_upvote, name='ans_upvote'),
    path('<ques_id>/downvote', views.ques_downvote, name='ques_downvote'),
    path('<ques_id>/<ans_id>/downvote', views.ans_downvote, name='ans_downvote')
]
