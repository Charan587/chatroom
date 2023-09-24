from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

@login_required
def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    # Check if the room already exists
    if Room.objects.filter(name=room_name).exists():
        room = Room.objects.get(name=room_name)

        # Remove previous users from the active_users field
        room.active_users.clear()

        # Add the current user to the room's active users
        room.active_users.add(request.user)

        return redirect('/' + room_name + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room_name)

        # Remove previous users from the active_users field
        new_room.active_users.clear()

        # Add the current user to the new room's active users
        new_room.active_users.add(request.user)

        return redirect('/' + room_name + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})