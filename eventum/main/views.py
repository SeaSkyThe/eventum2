from django.shortcuts import render
from event.models import Event
import datetime
from django.utils import timezone

# Create your views here.
#pagina inicial, aqui a gente faz o request dos eventos e exibe eles conforme o home.html
def homepage(request):

    now = timezone.now()

    #separando eventos que vao acontecer, eventos acontecendo, e eventos que ja aconteceram
    future_events = Event.objects.filter(start_datetime__gt = now) #start_datetime__gt = start_datetime greater than
    ongoing_events = Event.objects.filter(start_datetime__lte = now, end_datetime__gte = now) #lte = lass than or equal // gte = greater than or equal
    past_events = Event.objects.filter(end_datetime__lt = now, start_datetime__lt = now)

    #ordenando todos por data
    future_events = future_events.order_by('start_datetime')
    ongoing_events = ongoing_events.order_by('start_datetime')
    past_events = past_events.order_by('start_datetime')

    return render(request, 'main/home.html', {'future_events': future_events, 'ongoing_events':ongoing_events, 'past_events':past_events})
