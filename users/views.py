from __future__ import print_function
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, UserRoles, Mentor, pool_choices
from django.http import HttpResponseRedirect
from django.contrib import messages
from .UserForms import ChangeRolesForm, ChangeMentorStatus, AddMentor, AssignPools
from tasks.views import index

def userDetails(user_id):
    dict_profile = {}
    user = User.objects.get(id=user_id)
    dict_profile['id'] = user.id
    dict_profile['fname'] = user.first_name
    dict_profile['lname'] = user.last_name
    dict_profile['username'] = user.username
    dict_profile['email'] = user.email
    dict_profile['role'] = user.profile.role
    dict_profile['bdate'] = user.profile.Birth_date
    dict_profile['salary'] = user.profile.salary
    dict_profile['bonus'] = user.profile.bonus
    dict_profile['fine'] = user.profile.fine
    dict_profile['total_salary'] = user.profile.total_salary
    dict_profile['claimed'] = user.profile.claimed_tasks
    dict_profile['finished'] = user.profile.completed_tasks
    dict_profile['worked'] = user.profile.open_tasks
    try:
        dict_profile['avgworked'] = (dict_profile['worked'] / dict_profile['finished'])
    except:
        dict_profile['avgworked'] = 0

    return dict_profile

@login_required
def pool_status(request):
    if request.method == 'POST':
        posted_request = request.POST.dict()
        all_keys = list(posted_request.keys())
        usrname = all_keys[len(all_keys)-1]
        usr = User.objects.get(username=usrname)
        
        if(request.POST.get('mentors') == 'Select'):
            messages.warning(request, 'Please add a valid mentor!')
            return HttpResponseRedirect('/pool_status')
        print(type(usr.id))
        print(type(request.POST.get('mentors')))
        if(str(usr.id) == request.POST.get('mentors')):
            print("cAME HERE")
            messages.warning(request, 'Cannot assign the worker as a mentor to himself!')
            return HttpResponseRedirect('/pool_status')

        if(usr.profile.worker_pool==request.POST.get('radio') and request.POST.get('mentors') in usr.profile.get_mentors() ):
            messages.warning(request, 'Mentor already added!')
            return HttpResponseRedirect('/pool_status')
        

        if(request.POST.get('radio') == 'A'):
            usr.profile.set_mentors([request.POST.get('mentors')])
        else:
            original_mentors = usr.profile.get_mentors()
            if(usr.profile.worker_pool != request.POST.get('radio')):
                original_mentors = []
            
            original_mentors.append(request.POST.get('mentors'))   
            usr.profile.set_mentors(original_mentors)

        usr.profile.worker_pool = request.POST.get('radio')
        usr.profile.save()
        # set_pool = request.POST.get('pool')
        # selected_pool = set_pool
        # usr.profile.worker_pool = set_pool
        # usr.profile.save()

    user_dict=dict()
    users = User.objects.all()
    mentors = Mentor.objects.all()
    mentors_list = []
    mentor_form = [('Select','Select')]

    for mentor in mentors:
        # mentors_list.append(mentor.user.id)
        mentor_form.append((mentor.user.id,mentor.user.username))
    for usr in users:
        if (usr.profile.role == UserRoles.ADMIN.value):
            continue
        form = AssignPools(value=usr.id, mentors=mentor_form)
        current_mentors = []
        for mentor in usr.profile.get_mentors():
            current_mentors.append(User.objects.get(id=mentor))

        user_dict[usr.username] = {'form':form,'current_mentors':current_mentors}
        # print(user_dict[usr.username]['current_mentors'])

    return render(request, 'assign_workers_to_pool.html', {'user_dict':user_dict})

@login_required
def profileview(request):
    user_id = User.objects.get(username=request.user.username).id
    dict_profile = {}
    profile = Profile.objects.get(user_id=user_id).role

    if profile == UserRoles.ADMIN.value:
        emp_profile = {}
        profiles = Profile.objects.all()
        for worker in profiles:
            if worker.role == UserRoles.WORKER.value:
                profile_val = userDetails(worker.user_id)
                dict_profile[profile_val['username']] = profile_val

            elif worker.role != UserRoles.ADMIN.value:
                work_val = userDetails(worker.user_id)
                emp_profile[work_val['username']] = work_val
        return render(request, 'admin_view.html', {'dict_profile': dict_profile, 'emp_profile': emp_profile})

    else:
        dict_profile[request.user.username] = userDetails(user_id)
        return render(request, 'home.html', {'dict_profile': dict_profile})

@login_required
def change_roles(request):
    user = User.objects.get(username=request.user.username)
    profile = user.profile.role
    if profile != 'admin':
        messages.warning(request, 'Permission Denied!! You do not have permission to access this page')
        return HttpResponseRedirect('/')

    users = User.objects.all()
    if request.method == 'POST':
        posted_request = request.POST.dict()
        print(posted_request)
        all_keys = list(posted_request.keys())
        usrname = all_keys[len(all_keys)-1]
        usr = User.objects.get(username=usrname)
        previous_role = usr.profile.role
        usr.profile.role = posted_request['role']
        if (previous_role == UserRoles.WORKER.value) or (previous_role == UserRoles.AUDITOR.value):
            usr.profile.salary = posted_request['salary']
            usr.profile.bonus = posted_request['bonus']
            usr.profile.fine = posted_request['fine']
            usr.profile.audit_prob_user = posted_request['audit_prob']
        usr.profile.save()
        usr.profile.save()
    user_dict=dict()
    for usr in users:
        if (usr.profile.role == UserRoles.ADMIN.value):
            continue
        user_dict[usr.username] = ChangeRolesForm(value=usr.id)

    return render(request, 'changeRoles.html', {'user_dict':user_dict})


@login_required
def mentor_status(request):
    user = User.objects.get(username=request.user.username)
    profile = user.profile.role
    if profile != 'admin':
        messages.warning(request, 'Permission Denied!! You do not have permission to access this page')
        return HttpResponseRedirect('/')

    profiles = Profile.objects.all()
    mentors = Mentor.objects.all()

    mentors_list = []

    for mentor in mentors:
        mentors_list.append(mentor.user.username)

    if request.method == 'POST':
        posted_request = request.POST.dict()
        all_keys = list(posted_request.keys())
        usrname = all_keys[len(all_keys)-1]
        usr_id = User.objects.get(username=usrname).id
        worker = Profile.objects.get(user_id=usr_id)
        value = request.POST.get("mentor_status")
        if value == 'True':
            value = True
        else:
            value = False
        worker.is_Mentor = value
        worker.save()
        try:
            if not (value==True):
                print('deleting')
                usr = User.objects.get(username=usrname)
                Mentor.objects.get(user_id=usr_id).delete()
                usr.save()
                mentors = Mentor.objects.all()
                mentors_list = []
                for mentor in mentors:
                    mentors_list.append(mentor.user.username)
        except:
            pass
        try:
            if (value==True):
                print('creating')
                usr = User.objects.get(username=usrname)
                Mentor.objects.create(user=usr)
                usr.mentor.save()
                mentors = Mentor.objects.all()
                mentors_list = []
                for mentor in mentors:
                    mentors_list.append(mentor.user.username)
        except:
            pass

    worker_context = {}
    for profile in profiles:
        if profile.role == UserRoles.WORKER.value:
            worker_context[profile.user.username] = ChangeMentorStatus(value=profile.user.profile.is_Mentor)

    return render(request, 'mentorStatus.html', {'user_dict': worker_context})




@login_required
def change_mentor(request, usrname):
    user = User.objects.get(username=request.user.username)
    profile = user.profile.role
    if profile != 'admin':
        messages.warning(request, 'Permission Denied!! You do not have permission to access this page')
        return HttpResponseRedirect('/')

    usr = User.objects.get(username=usrname)
    usrid = usr.id
    usr_mentors = usr.profile.get_mentors()

    mentors = Mentor.objects.all()
    mentors_list = []
    mentor_form = []

    for mentor in mentors:
        mentors_list.append(mentor.user.id)
        mentor_form.append((mentor.user.id,mentor.user.username))

    cur_mentor = usr.profile.get_mentors()
    submitted = False
    same_mentor = False

    if request.method == 'POST':

        set_mentor = request.POST.get('mentor_ch')
        set_pool = request.POST.get('pool')
        selected_pool = set_pool
        usr_mentors = usr.profile.get_mentors()
        print(usr_mentors)

        if set_mentor == 'Select':
            submitted = True
        else:
            if set_pool == usr.profile.worker_pool and set_mentor in cur_mentor:
                same_mentor = True
            else:
                if (usr.profile.worker_pool != selected_pool) or (selected_pool=='A'):
                    for usrid in usr_mentors:
                        cur_mentor = User.objects.get(id=usrid)
                        if usr.id in cur_mentor.profile.get_mentees():
                            print('removing mentor')
                            cur_mentor.profile.set_mentees(cur_mentor.profile.get_mentees().remove(usr.id))
                            cur_mentor.profile.save()
                    usr_mentors = [set_mentor]
                    cur_mentor = User.objects.get(id=set_mentor)
                    if usr.id not in cur_mentor.profile.get_mentees():
                        cur_mentees = cur_mentor.profile.get_mentees()
                        cur_mentees.append(usr.id)
                        cur_mentor.profile.set_mentees(cur_mentees)
                        cur_mentor.profile.save()
                        print(cur_mentor.profile.get_mentees())
                else:
                    new_mentor = set_mentor
                    usr_mentors.append(new_mentor)
                    mentor_user = User.objects.get(id=new_mentor)
                    mentees_list = mentor_user.profile.get_mentees()
                    if usrid not in mentees_list:
                        mentees_list.append(usrid)
                    mentor_user.profile.set_mentees(mentees_list)
                    mentor_user.profile.save()
                usr.profile.worker_pool = set_pool
                usr.profile.save()
                usr.profile.set_mentors(usr_mentors)
                usr.profile.save()


    cur_mentor = usr.profile.get_mentors()
    new_form = AddMentor(mentor_choices=mentor_form, pool=usr.profile.worker_pool,
                         cur_mentor=cur_mentor,submitted= submitted, same_mentor=same_mentor)
    new_form.full_clean()
    cur_mentor_user = []
    for mentor in cur_mentor:
        cur_mentor_user.append(User.objects.get(id=mentor))

    return render(request, 'changeMentor.html', {'username':usrname, 'cur_mentor': cur_mentor_user, 'form':new_form})
