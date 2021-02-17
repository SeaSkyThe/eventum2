from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Título', max_length=100, null=False)
    start_datetime = models.DateTimeField(verbose_name='Início', null=False)
    end_datetime = models.DateTimeField(verbose_name='Fim', null=False)
    activity_limit = models.IntegerField(verbose_name='Limite de atividades para inscrição', null=True,
                                         help_text='Para eventos sem limite de atividades, use 0.')

    def __str__(self):
        return self.title



class Organize_Event(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, verbose_name='Usuário')
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING, verbose_name='Evento')

    def __str__(self):
        return f'{self.user_id} - {self.event_id}'


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name='Título', max_length=100, null=False)
    location = models.CharField(verbose_name='Localização',
                                help_text='Local onde o evento ocorrerá. Pode ser um endereço, uma sala, etc.',
                                max_length=255, null=False)
    start_datetime = models.DateTimeField(verbose_name='Início', null=False)
    end_datetime = models.DateTimeField(verbose_name='Fim', null=False)
    cost = models.FloatField(verbose_name='Valor (R$)', null=False)
    description = models.CharField(verbose_name='Descrição', max_length=255, null=True)
    subscription_limit = models.IntegerField(verbose_name='Limite de inscrições', null=True, default=0,
                                             help_text='Para atividades sem limite de inscrições, use 0.')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('activity')
        verbose_name_plural = _('activities')
