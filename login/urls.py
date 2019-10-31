from django.urls import path
from .views import signup, logoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns = [
    path('accounts/login/',auth_views.LoginView.as_view(template_name="login.html"), {'next_page': '/'}, name='login'),
    path('signup/',signup, name = 'signup'),
    path('logout/',logoutView, name='logout')
]
