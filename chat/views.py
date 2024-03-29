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
    participant_count=1
    user = User.objects.get(username=request.user.username)
    #print(user)
    tuj_list =TaskUserJunction.objects.filter(worker_id = user)
    #role = request.user.profile.role
    role=request.session['role']
    #print(role)
    participants = Profile.objects.filter(user_id=request.user.profile.user_id)
    mentee_task_list = {};
    workername = None
    #mentor_boolean  = 'false';
    for p in participants:
        # if(p.is_Mentor):
        #     mentor_boolean = 'true';
        # else:
        #     mentor_boolean = 'false';
        if(role == 'mentor'):
           try:
               mentee_id = p.get_mentees();
               for m in mentee_id:
                   user = User.objects.get(id=m);
                   participant_count=1
                   workername=user.username
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
               workername=p.user
               mentor_id = p.get_mentors()[0];
               participant_count=len(p.get_mentors())
               if(participant_count==1):
                  user = User.objects.get(id=mentor_id);
                  chat_participants.append(user.username);
               else:
                  chat_participants.append("Sam")
           except:
               tuj_list=tuj_list
            
    # Render that in the index template
    return render(request, "messages.html", {
        "tuj_list": tuj_list,
        "chat_participants" : chat_participants,
        "participant_count" : participant_count,
        "mentee_task_list" : mentee_task_list,
        "workername" : workername,
        "role" : role,
        "curr" : user
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
    role=request.session['role']
    pool='A'
    participants = Profile.objects.filter(user_id=request.user.profile.user_id)
    try:
        user_message_thread = Messages.objects.all();
        room_id = request.GET.get('room_id');
        for thread in user_message_thread:
            username = User.objects.get(id=thread.sender_id);
            thread_id = str(thread.room_id);
            if(thread_id == room_id):
                worker_message_list[thread.id] = [str(username),thread.text,thread.star];
                #message_thread_id+=1;
        if(role =='worker'):
            curr=User.objects.get(username=request.user.username)
            curr=str(curr)
            senders=list(worker_message_list.values())
            participants = Profile.objects.filter(user_id=request.user.profile.user_id)
            for p in participants:
              pool=p.worker_pool
            if pool=='B':
              for l in worker_message_list:
                    if(worker_message_list[l][0]!=curr):
                        worker_message_list[l][0]='Sam'
    except:
        worker_message_list = worker_message_list
    print(worker_message_list)
    return JsonResponse(worker_message_list,safe=False);
@login_required
def update_message(request):
  x=request.GET.get('message_id');
  x=int(x[11:])
  print(x)
  message=Messages.objects.filter(id=x).update(star=request.GET.get('star'));

@login_required
def fetch_message(request):
  star=request.GET.get('star');
  room_id=request.GET.get('room_id');
  messages=Messages.objects.filter(room_id=room_id,star=star)
  #print(messages);
  starMessagesDict=[];
  for m in messages:
    username = User.objects.get(id=m.sender_id);
    temp=(str(username),m.text,m.room_id);
    starMessagesDict.append(temp);
    #print(m.text)
  print(starMessagesDict)
  return JsonResponse(starMessagesDict,safe=False);

