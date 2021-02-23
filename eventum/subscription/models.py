from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Subscription_Type(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING, verbose_name='Evento')
    description = models.CharField(max_length=255, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        return f'{self.description} ({self.event_id})'


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    subscription_type_id = models.ForeignKey('subscription.Subscription_Type', on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        return f'{self.user_id} - {self.event_id}'


class Subscription_Activity(models.Model):
    activity_id = models.ForeignKey('event.Activity', on_delete=models.DO_NOTHING)
    subscription_id = models.ForeignKey('subscription.Subscription', on_delete=models.DO_NOTHING)
    cost = models.FloatField(null=False)

    class Meta:
        verbose_name = _('subscription_activity')
        verbose_name_plural = _('subscription_activities')
