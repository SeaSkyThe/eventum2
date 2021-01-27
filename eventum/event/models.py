from django.db import models

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)
    activity_limit = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Organize_Event(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)
   

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=255, null=False)
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)
    cost = models.FloatField(null=False)
    description = models.CharField(max_length=255, null=True)
    subscription_limit = models.IntegerField(null=True)