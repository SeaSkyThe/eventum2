from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homepage, name='index'), #pagina inicial
    path('<int:pk>/', views.event_detail, name='event_detail'),
]
