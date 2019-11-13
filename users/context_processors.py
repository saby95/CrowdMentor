from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from users.models import UserRoles

def view(request):
    dict_functs = {}
    broadcast_count = ''
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user_id = user.id
        profile = user.profile.get_roles()
        # Session value will always be populated from the / page of each of the user roles
        profile = request.session['role']
        
        #broadcast_messages_count = BroadcastMessages.objects.filter(group_role=profile, claim=False).count()
        #broadcast_count = 'Broadcast(' + str(broadcast_messages_count) + ')'
        if profile == UserRoles.TASK_UPDATER.value:
            dict_functs['/tasks/add_tasks']= 'Add task'
            dict_functs['/tasks/'] = 'View task'
            dict_functs['/help/'] = 'Help'

        if profile == UserRoles.ADMIN.value:
            dict_functs['/change_roles'] = 'Update Worker'
            # dict_functs['/mentor_status'] = 'Mentor Status' #Not needed as it is covered in the Update Worker page
            dict_functs['/pool_status'] = 'Assign pools'
            dict_functs['/messages/'] = 'Messages'
            dict_functs['/help/'] = 'Help'

        if profile == UserRoles.WORKER.value:
            dict_functs['/tasks/claimed/'] = 'Claimed tasks'
            dict_functs['/tasks/'] = 'Open tasks'
            dict_functs['/messages/'] = 'Messages'
            dict_functs['/help/'] = 'Help'

        if profile == UserRoles.AUDITOR.value:
            dict_functs['/tasks/open_audits/'] = 'Open Audits'
            dict_functs['/tasks/audits/'] = 'Claimed Audits'
            dict_functs['/help/'] = 'Help'

        if profile == UserRoles.MENTOR.value:
            dict_functs['/messages/'] = 'Messages'
            dict_functs['/tasks/task_status/'+str(user_id)+'/'] = 'Task Status'
            dict_functs['/help/'] = 'Help'
        # New dictionary to store the updated urls (with the roles)
        dictionary = {}    
        if('role' in request.session): 
            for x,y in dict_functs.items():
                x = x + '?role='+ request.session['role']
                dictionary[x] = y

        else:
            dictionary = dict_functs
  
    else:
        dictionary = {}
        dict_functs['/accounts/login'] = 'Login'
        dict_functs['/signup'] = 'Signup'
        dictionary = dict_functs
    return {"dict_functs" : dictionary}

