from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name =  models.CharField(verbose_name='Nome de usuário', max_length=60, null=False)
    password = models.CharField(verbose_name='Senha', max_length=45, null=False)
    show_name = models.CharField(verbose_name='Nome de exibição', help_text='Este será o nome exibido no seu perfil.',
                                 max_length=60, null=True)
    email = models.CharField(verbose_name='E-mail', max_length=45, null=True)
    phone = models.CharField(verbose_name='Telefone', max_length=20, null=True)
    street = models.CharField(verbose_name='Rua', max_length=255, null=True)
    house_number = models.IntegerField(verbose_name='Número', null=True)
    complement = models.CharField(verbose_name='Complemento', help_text='Número do apartamento, ponto de referência, bloco, etc.', max_length=255, null=True)
    district = models.CharField(verbose_name='Cidade', max_length=100, null=True)
    CEP = models.CharField(max_length=20, null=True)
    CPF = models.CharField(help_text='Apenas números', max_length=12, null=True)
    active = models.BooleanField(verbose_name='Usuário ativo', null=True, default=True)
    type_organizer = models.BooleanField(verbose_name='É Organizador', null=True, default=False)
    type_participant = models.BooleanField(verbose_name='É Participante', null=True, default=False)
    link = models.CharField(verbose_name='Link', max_length=255, null=True, blank=True)
    profile_picture = models.CharField(verbose_name='Foto de perfil', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user_name
