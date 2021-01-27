from django.contrib import admin
from .models import Event, Organize_Event, Activity

# Register your models here.
admin.site.register(Event)
admin.site.register(Organize_Event)
admin.site.register(Activity)