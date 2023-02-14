from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chat/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

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
