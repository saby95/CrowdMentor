from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from users.models import UserRoles
from django.shortcuts import HttpResponseRedirect

from .loginForms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Birth_date = form.cleaned_data.get('birth_date')
            if form.cleaned_data.get('role') == UserRoles.TASK_UPDATER.value:
                user.profile.role = UserRoles.TASK_UPDATER.value
            elif form.cleaned_data.get('role') == UserRoles.AUDITOR.value:
                user.profile.role = UserRoles.AUDITOR.value
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logoutView(request):
   logout(request)
   return HttpResponseRedirect('/')




