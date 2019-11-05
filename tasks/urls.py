from django.urls import path

from . import views

pathpatterns = [
    path('', views.index, name='index'),
    path('add_tasks/', views.add_tasks, name='add_tasks'),
    path('(?P<task_id>[0-9]+)/', views.detail, name='detail'),
    path('claimed/', views.claimed_tasks, name='claimed_tasks'),
    path('(?P<task_id>[0-9]+)/claim', views.claim, name='claim'),
    path('claimed/(?P<task_id>[0-9]+)/answer', views.answer, name='answer'),
    path('audits/', views.audit_tasks, name='audit_tasks'),
    path('open_audits/', views.open_audits, name='open_audits'),
    path('audits/(?P<task_id>[0-9]+)/claim_audit', views.claim_audit, name='claim_audit'),
    path('audits/(?P<task_id>[0-9]+)/submit_audit', views.submit_audit, name='submit_audit'),
    path('open_audits/(?P<task_id>[0-9]+)/', views.detail_audit, name='detail_audit'),
    path('task_status/(?P<user_id>[0-9]+)/', views.task_status, name='task_status'),
    path('all_task_status/', views.all_task_status, name='all_task_status'),
    path('view_task/(?P<user_id>[0-9]+)/(?P<task_id>[0-9]+)/', views.view_task, name='view_task'),
]
