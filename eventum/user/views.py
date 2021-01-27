from django.shortcuts import render

# Create your views here.

# Listar eventos de um determinado organizador
def event_list_organizer(request, organizer_id):
    events = Event.objects.raw('''SELECT * FROM event_event LEFT JOIN event_organize_event on
                                (event_organize_event.event_id = event_event.id AND event_organize_event.user_id = %s)''', [organizer_id])
    return render(request, 'event_list.html', {'events': events})

# Listar eventos que um usuário está inscrito
def event_list_user(request, participant_id):
    events = Event.objects.raw('''SELECT * FROM event_event LEFT JOIN subscription_subscription on
                                (subscription_subscription.event_id = event_event.id AND subscription_subscription.user_id = %s)''', [participant_id])
    return render(request, 'event_list.html', {'events': events})

# Listar atividades dos eventos que um participante está participando
def event_activity_list_participant(request, user_id):
    events = Event.objects.raw('''SELECT event_activity.id, event_activity.title,
                                event_activity.location, event_activity.start_datetime,
                                event_activity.end_datetime,
                                event_activity.description,
                                event_activity.subscription_limit,
                                subscription_subscription_activity.cost, event_event.id,
                                event_event.title FROM event_activity LEFT JOIN
                                subscription_subscription on (subscription_subscription.user_id =
                                %s) LEFT JOIN subscription_subscription_activity
                                on (subscription_subscription_activity.activity_id =
                                event_activity.id AND
                                subscription_subscription_activity.subscription_id =
                                subscription_subscription.id) LEFT JOIN event_event on
                                (event_event.id = subscription_subscription.event_id) ORDER BY
                                event_event.id''', [user_id])
    return render(request, 'event_list.html', {'events': events})

# Verificar histórico de eventos participados
def event_list_participant_historic(request, user_id):
    events = Event.objects.raw('''SELECT
                                event_event.id,
                                event_event.title,
                                event_event.start_datetime,
                                event_event.end_datetime,
                                subscription_subscription.cost,
                                subscription_subscription.date,
                                subscription_subscription_type.description,
                                (SELECT
                                count(subscription_subscription_activity.activity_id)
                                FROM subscription_subscription_activity WHERE
                                subscription_subscription_activity.subscription_id =
                                subscription_subscription.id) as atividades_inscritas,
                                FROM event_event
                                INNER JOIN subscription_subscription on
                                (subscription_subscription.event_id = event_event.id AND
                                subscription_subscription.user_id = %s)
                                LEFT JOIN subscription_subscription_type on
                                (subscription_subscription_type.id =
                                subscription_subscription.subscription_type_id)''', [user_id])
    return render(request, 'event_list.html', {'events': events})
