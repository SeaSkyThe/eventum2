from django.shortcuts import render
from event.models import Event

# Create your views here.
#pagina inicial, aqui a gente faz o request dos eventos e exibe eles conforme o home.html
def homepage(request):
    events = Event.objects.all()
    return render(request, 'main/home.html', {'events': events})
