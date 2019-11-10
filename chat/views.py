from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from tasks.models import ResearchTasks,TaskUserJunction
from django.contrib.auth.models import User
from profile import Profile


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")
    roomslist = [];
    user = User.objects.get(username=request.user.username)
    tuj_list =TaskUserJunction.objects.filter(worker_id = user)
    """roomslist = [];
    for room in rooms:
        roomslist.append(room.title)
    for tuj in tuj_list:
        if(str(tuj) not in roomslist):
            room = Room(title=tuj, staff_only=False)
            room.save()
            roomslist = (Room.objects.values_list('title', 'id'));
            roomId = roomslist[len(roomslist)-1][1];
            TaskUserJunction.objects.filter(task_id_id=tuj.task_id.id).update(room_id=roomId)"""
            
    # Render that in the index template
    return render(request, "messages.html", {
        "tuj_list": tuj_list,
    })
