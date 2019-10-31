from django.urls import path
from .views import profileview, change_roles

urlpatterns = [
    path('', profileview, name='view'),
    path('change_roles/', change_roles,name='ChangeUserRoles')
]
