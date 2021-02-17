from django.shortcuts import *

#Importando o Model USER
from user.models import User

from django.views.generic import View

#Importando form personalizado
from user.forms import SignUpForm
#Importando bibliotecas para autenticação
from django.contrib.auth import logout, authenticate, login
# Create your views here.
#view que irá ficar responsavel pelo cadastro do usuário

# TODO: TENTAR APENAS CRIAR UM USUARIO NOSSO NOVO COM O QUE FOI PEGO NO FORM, E USAR O ESQUEMA DE AUTENTICAÇÃO DO USER DO PROPRIO DJANGO

def SignUp(request):
    form = SignUpForm()
    if(request.method == "POST"):
        form = SignUpForm(request.POST)
    elif(request.method == "GET"):
        return render(request = request,
            template_name = "subscription/signup.html")


    if(form.is_valid()):
        user = form.save()
        #editando manualmente o nome de perfil para o username, caso nenhum seja passado
        
        #definindo que o usuario é participante ao se cadastrar.
        user.type_participant = True

        user.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/login')
    else:
        return render(request = request,
            template_name = "subscription/signup.html",
            context={"form":form})


def Login(request):
    return render(request = request,
        template_name = "subscription/login.html")

def Logout(request):
    logout(request)
    return render(request = request,
        template_name = "/")
