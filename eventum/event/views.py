from django.shortcuts import render, get_object_or_404
from .models import Event
from django.utils import timezone

# Create your views here.

# Listar eventos disponíveis
def event_list(request):
    events = Event.objects.raw('SELECT * FROM event_event WHERE start_datetime >= %s', [timezone.now()])
    return render(request, 'event_list.html', {'events': events})

# Listar um evento em específico
def event_detail(request, pk):
    event = Event.objects.raw('SELECT * FROM event_event WHERE id = %s', [pk])[0]
    return render(request, 'event_detail.html', {'event': event})

# Listar eventos que estão ocorrendo em um determinado período
def event_list_range(request, start, end):
    events = Event.objects.raw('SELECT * FROM event_event WHERE start_datetime >= %s AND end_datetime <= %s', [start, end])
    return render(request, 'event_list.html', {'events': events})

# Listar participantes de um evento
def event_list_participants(request, event_id):
    events = Event.objects.raw('''SELECT * FROM user_user LEFT JOIN subscription_subscription
                                on (user_user.id = subscription_subscription.user_id) WHERE
                                subscription_subscription.event_id = %s''', [event_id])
    return render(request, 'event_list.html', {'events': events})

# Listar participantes de uma atividade
def event_activity_list_participants(request, activity_id):
    events = Event.objects.raw('''SELECT user_user.id, user_user.show_name,
                                user_user.profile_picture FROM user_user LEFT JOIN
                                subscription_subscription on (subscription_subscription.user_id =
                                user_user.id) LEFT JOIN subscription_subscription_activity on
                                (subscription_subscription_activity.subscription_id =
                                subscription_subscription.id) WHERE
                                subscription_subscription_activity.activity_id =
                                %s AND user_user.active = TRUE''', [activity_id])
    return render(request, 'event_list.html', {'events': events})
