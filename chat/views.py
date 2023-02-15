from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

@login_required
def chat(request, slug=''):
    room_selected = None
    messages = None
    if slug != '':
        room_selected = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=room_selected)[0:25]
    
    rooms = Room.objects.all()
    
    return render(request, 'chat/chat.html', {
        'room_selected': room_selected,
        'chats': messages,
        'rooms': rooms
    })
