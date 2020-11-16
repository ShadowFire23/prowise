from django.shortcuts import render, get_object_or_404
from .models import Event

def event_list(request):
    events_f = Event.objects.filter(status=False)
    events_t = Event.objects.filter(status=True)
    return render(request, 'etkinlik/event_list.html', {'events_f':events_f , 'events_t':events_t})

def event_detail(request, url_sistem):
    event = get_object_or_404(Event, url_sistem=url_sistem)

    return render(request, 'etkinlik/event_detail.html',{'event':event})
