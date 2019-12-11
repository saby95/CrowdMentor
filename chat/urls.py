from django.urls import path

from . import views

urlpatterns =[
    path('',views.index),
    path('save_message/',views.save_message,name='save_message'),
    path('message_thread/',views.message_thread,name='message_thread'),
    path('update_message/',views.update_message,name='update_message'),
    path('fetch_message/',views.fetch_message,name='fetch_message')
]
