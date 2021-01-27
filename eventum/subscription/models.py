from django.db import models
from django.utils import timezone

# Create your models here.
class Subscription_Type(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, null=False)
    cost = models.FloatField(null=False)


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    subscription_type_id = models.ForeignKey('subscription.Subscription_Type', on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now, null=False)
    cost = models.FloatField(null=False)


class Subscription_Activity(models.Model):
    activity_id = models.ForeignKey('event.Activity', on_delete=models.DO_NOTHING)
    subscription_id = models.ForeignKey('subscription.Subscription', on_delete=models.DO_NOTHING)
    cost = models.FloatField(null=False)