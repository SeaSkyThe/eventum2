from django.shortcuts import *

#Importando o Model USER
from user.models import User

from django.views.generic import View

#Importando form personalizado
from user.forms import SignUpForm
#Importando bibliotecas para autenticação
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
#view que irá ficar responsavel pelo cadastro do usuário

#REGISTRO DO USUARIO NO SISTEMA
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
        print(authenticate(username=username, password=password))
        login(request, user)



        return render(request = request,
            template_name = "main/home.html",
            context={"user":user, "form":form})
    else:
        return render(request = request,
            template_name = "subscription/signup.html",
            context={"form":form})


#LOGIN DO USUARIO NO SISTEMA
# def Login(request):
#     # form = AuthenticationForm()
#     # if(request.method == "POST"):
#     #     form = AuthenticationForm(request.POST)
#     #     print("ENTROU AQUI")
#     # print(form)
#     # if(form.is_valid()):
#     #     username = form.username
#     #     password = form.password
#     #     print("ENTROU AQUI 2")
#     #     user = authenticate(username=username, password=password)
#     #     login(request, user)
#     #     return redirect('a')
#
#     return render(request = request, template_name = "subscription/login.html", context={"form":form})

def logout_request(request):
    logout(request)
    message.info(request, "Logout realizado com sucesso!")
    return redirect("/login")
