from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_tasks/', views.add_tasks, name='add_tasks'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('claimed/', views.claimed_tasks, name='claimed_tasks'),
    path('<int:task_id>/claim', views.claim, name='claim'),
    path('claimed/<int:task_id>/answer', views.answer, name='answer'),
    path('audits/', views.audit_tasks, name='audit_tasks'),
    path('open_audits/', views.open_audits, name='open_audits'),
    path('audits/<int:task_id>/claim_audit', views.claim_audit, name='claim_audit'),
    path('audits/<int:task_id>/submit_audit', views.submit_audit, name='submit_audit'),
    path('open_audits/<int:task_id>/', views.detail_audit, name='detail_audit'),
    path('task_status/<int:user_id>/', views.task_status, name='task_status'),
    path('all_task_status/', views.all_task_status, name='all_task_status'),
    path('view_task/<int:user_id>/<int:task_id>/', views.view_task, name='view_task'),
]
