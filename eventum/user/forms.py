from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User


#FORMULARIO PARA REGISTRAR O USUÁRIO - FALTANDO NOME COMPLETO?
class SignUpForm(UserCreationForm):
    username =  forms.CharField(max_length=60)  #existe o parametro "help_text"
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(max_length=45)
    password2 = forms.CharField(max_length=45)
    email = forms.EmailField(max_length=45)
    phone = forms.CharField(max_length=20)
    street = forms.CharField(max_length=255)
    house_number = forms.IntegerField()
    complement = forms.CharField(max_length=255)
    district = forms.CharField(max_length=100)
    CEP = forms.CharField(max_length=20)
    CPF = forms.CharField(max_length=12)
    link = forms.CharField(max_length=255, required=False)
    profile_picture = forms.CharField(max_length=255, required=False)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'street', 'house_number',
                  'complement', 'district', 'CEP', 'CPF', 'link', 'profile_picture')


#FORMULARIO DE LOGIN DO USUARIO
