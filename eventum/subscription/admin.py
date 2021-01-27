from django.contrib import admin
from .models import Subscription_Type, Subscription, Subscription_Activity

# Register your models here.
admin.site.register(Subscription_Type)
admin.site.register(Subscription)
admin.site.register(Subscription_Activity)
