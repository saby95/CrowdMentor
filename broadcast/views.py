# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import BroadcastMessages
from privatemessages.models import Thread

@login_required
def index(request):
    user = User.objects.get(username=request.user.username)
    role = user.profile.role
    broadcast_messages = BroadcastMessages.objects.filter(group_role=role, claim=False)

    context = {
        'broadcast_messages': broadcast_messages,
    }
    return render(request, 'broadcast/index.html', context)

@login_required
def claim(request, broadcast_id, thread_id):
    broadcast = get_object_or_404(BroadcastMessages, id=broadcast_id)
    broadcast.claim = True
    broadcast.claim_by = request.user
    broadcast.save()

    thread = get_object_or_404(
        Thread,
        id=thread_id
    )
    thread.participants.add(request.user)
    thread.save()

    return redirect('chat_view', thread_id=thread_id)

@login_required
def broadcast_count(request):
    cnt = BroadcastMessages.objects.filter(group_role=request.user.profile.role, claim=False).count()
    return HttpResponse(cnt, content_type="text/plain")