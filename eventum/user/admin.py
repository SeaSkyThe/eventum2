from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('active', 'type_organizer', 'type_participant')
    list_display = ('user_name', 'email', 'active', 'phone', 'type_organizer', 'type_participant')

    fieldsets = (

        ('Credenciamento', {
            'fields': ('user_name', 'password')
        }),
        ('Dados pessoais', {
            'fields': ('show_name', 'email', 'phone', ('district', 'CEP'), ('street', 'house_number', 'complement'), 'CPF')
        }),
        ('Configurações', {
            'fields': ('active', 'type_organizer', 'type_participant', ('link', 'profile_picture'))
        })
    )
