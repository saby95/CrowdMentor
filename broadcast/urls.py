from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<broadcast_id>[0-9]+)/(?P<thread_id>[0-9]+)/claim$', views.claim, name='claim'),
    url(r'^broadcast_count$', views.broadcast_count, name='broadcast_count'),
    ]