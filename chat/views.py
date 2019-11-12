from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Messages
from tasks.models import ResearchTasks,TaskUserJunction
from django.contrib.auth.models import User
from users.models import Profile
from django.http import HttpResponse,JsonResponse


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
           try:
               mentee_id = p.get_mentees();
               for m in mentee_id:
                   user = User.objects.get(id=m);
                   tuj_list = TaskUserJunction.objects.filter(worker_id = user)
                   chat_participants.append(user.username);
                   
                   task_list = [];
                   for tuj in tuj_list:
                       task_list.append((str(tuj),tuj.room_id));
                   mentee_task_list[user.username] = task_list;
           except:
               mentee_task_list={}
        else:
           #Get Mentors list
           try:
               mentor_id = p.get_mentors()[0];
               user = User.objects.get(id=mentor_id);
               chat_participants.append(user.username);
           except:
               tuj_list=tuj_list


            
    # Render that in the index template
    return render(request, "messages.html", {
        "tuj_list": tuj_list,
        "chat_participants" : chat_participants,
        "isMentor" : mentor_boolean,
        "mentee_task_list" : mentee_task_list
    })

@login_required
def save_message(request):
   import datetime
   current_message = (request.GET.get('message'));
   current_sender_id= request.user.profile.user_id;
   current_datetime = datetime.datetime.now();
   current_room_id = 0
   room_objects= Room.objects.filter(id= request.GET.get('room_id'))

   for room in room_objects:
       messages = Messages(text=current_message, datetime=current_datetime, sender_id = current_sender_id,room_id=room.id)
       messages.save()
   
   
   return HttpResponse("")
@login_required
def message_thread(request):
    import json
    messages_list = [];
    message_response = {};
    worker_message_list = {};
    message_thread_id = 1;
    try:
        user_message_thread = Messages.objects.all();
        room_id = request.GET.get('room_id');
        for thread in user_message_thread:
            username = User.objects.get(id=thread.sender_id);
            thread_id = str(thread.room_id);
            if(thread_id == room_id):
                worker_message_list[message_thread_id] = [str(username),thread.text];
                message_thread_id+=1;
    except:
        worker_message_list = worker_message_list
    return JsonResponse(worker_message_list,safe=False);
