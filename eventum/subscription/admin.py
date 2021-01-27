from django.contrib import admin
from .models import Subscription_Type, Subscription, Subscription_Activity

# Register your models here.
@admin.register(Subscription_Type)
class Subscription_TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_id', 'description', 'cost')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'subscription_type_id', 'date' , 'cost')

@admin.register(Subscription_Activity)
class Subscription_ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'subscription_id' , 'cost')
