from django.contrib import admin
from .models import Event, Organize_Event, Activity

# Register your models here.
@admin.register(Organize_Event)
class Organize_EventAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'event_id')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_filter = ('start_datetime', 'end_datetime')
    list_display = ('title', 'cost', 'start_datetime', 'end_datetime', 'subscription_limit')

class ActivityInline(admin.TabularInline):
    model = Activity

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ('start_datetime', 'end_datetime')
    list_display = ('title', 'start_datetime', 'end_datetime', 'activity_limit')
    inlines = [ActivityInline]
