from django.shortcuts import render, get_object_or_404
from .models import Event

def event_list(request):
    events_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events_list})

def event_details(request, pk):  # Ensure the function name matches the URL pattern
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_details.html', {'event': event})  # Ensure the template name is correct