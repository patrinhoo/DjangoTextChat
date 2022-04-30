from django.shortcuts import redirect
from django.views.generic import TemplateView

from .models import Room, Message


# Create your views here.
class HomeView(TemplateView):
    template_name = 'chat/home.html'

    def post(self, request, *args, **kwargs):
        room = self.request.POST.get('room_name')
        username = self.request.POST.get('username')

        if room:
            if Room.objects.filter(name=room).exists():
                return redirect(f'/{room}/?username={username}')
            else:
                new_room = Room.objects.create(name=room)
                new_room.save()
                return redirect(f'/{room}/?username={username}')
        else:
            return redirect('home')


class RoomView(TemplateView):
    template_name = 'chat/room.html'

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('username') and Room.objects.filter(name=request.get_full_path()[1:].split('/')[0]).exists():
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')

    def get_context_data(self, room, *args, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=room)
        context['username'] = self.request.GET.get('username')
        context['room'] = room

        return context
