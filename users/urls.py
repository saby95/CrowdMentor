from django.urls import path
from .views import profileview, change_roles, mentor_status, change_mentor, pool_status

urlpatterns = [
    path('', profileview, name='view'),
    path('change_roles/', change_roles,name='ChangeUserRoles'),
    path('mentor_status/', mentor_status,name='MentorStatus'),
    path('change_mentor/<usrname>/', change_mentor, name='ChangeMentor'),
    path('pool_status/', pool_status, name='PoolStatus')
]
