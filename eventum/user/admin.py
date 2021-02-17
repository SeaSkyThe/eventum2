from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('active', 'type_organizer', 'type_participant')
    list_display = ('username', 'email', 'active', 'phone', 'type_organizer', 'type_participant')

    fieldsets = (

        ('Credenciamento', {
            'fields': ('username', 'password')
        }),
        ('Dados pessoais', {
            'fields': ('first_name', 'last_name', 'email', 'phone', ('district', 'CEP'), ('street', 'house_number', 'complement'), 'CPF')
        }),
        ('Configurações', {
            'fields': ('active', 'type_organizer', 'type_participant', ('link', 'profile_picture'))
        })
    )
