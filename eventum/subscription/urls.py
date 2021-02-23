from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path("logout/", views.logout_request, name='logout'),

]
