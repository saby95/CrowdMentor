from django.urls import path

from . import views

urlpatterns =[
    path('',views.index),
    path('save_message/',views.save_message,name='save_message')
]
