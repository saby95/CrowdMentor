from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from tasks.models import ResearchTasks,TaskUserJunction
from django.contrib.auth.models import User
from users.models import Profile


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    import json
    rooms = Room.objects.order_by("title")
    roomslist = []
    chat_participants = []
    user = User.objects.get(username=request.user.username)
    tuj_list =TaskUserJunction.objects.filter(worker_id = user)
    role = request.user.profile.role
    participants = Profile.objects.filter(user_id=request.user.profile.user_id)
    mentee_task_list = {};
    mentor_boolean  = 'false';
    for p in participants:
        if(p.is_Mentor):
            mentor_boolean = 'true';
        else:
            mentor_boolean = 'false';
        if(p.is_Mentor == True):
            mentee_id = p.get_mentees();
            #print(mentee_id);
            for m in mentee_id:
                user = User.objects.get(id=m);
                tuj_list = TaskUserJunction.objects.filter(worker_id = user)
                chat_participants.append(user.username);
                
                task_list = [];
                for tuj in tuj_list:
                    task_list.append((str(tuj),tuj.room_id));
                mentee_task_list[user.username] = task_list;
        else:
            mentor_id = p.get_mentors()[0];
            user = User.objects.get(id=mentor_id);
            chat_participants.append(user.username);

    print(mentee_task_list)
            
    # Render that in the index template
    return render(request, "messages.html", {
        "tuj_list": tuj_list,
        "chat_participants" : chat_participants,
        "isMentor" : mentor_boolean,
        "mentee_task_list" : mentee_task_list
    })
