import re

from django.db import models

from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

#User Manager - Classe que vai disponibilizar funções para criação e administração de usuarios
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('O nome de usuário deve ser definido'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self._create_user(username=username, email=email, password=password, is_staff=False, is_superuser=False, **extra_fields)
        #atualizando manualmente os campos que não entram no cadastro
        user.type_participant = True
        #retornando o usuario
        return user

    def create_superuser(self, username, email, password, **extra_fields):

        user=self._create_user(username=username, email=email, password=password, is_staff=True, is_superuser=True, **extra_fields)

        #atualizando manualmente os campos que não entram no cadastro
        user.is_active = True
        user.type_organizer = True
        #salvando as mudanças no banco
        user.save(using=self._db)
        #retornando usuario
        return user

#SUBSTITUINDO O MODEL User do Django

#MUDANÇAS FEITAS NA TABELA DE USUÁRIOS: EXCLUIDO O CAMPO SHOW_NAME: USERNAME ESTÁ SENDO UTILIZADO NO LUGAR DELE
                # PARA O NOME DO USUÁRIO, ESTÃO SENDO UTILIZADOS OS CAMPOS FIRST_NAME E LAST_NAME
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)


    #password = models.CharField(verbose_name='Senha', max_length=45, null=False) #comentado pois ja existe
    # show_name = models.CharField(verbose_name='Nome de exibição (nickname)', null=True,
    #                              max_length=60,unique=True, help_text=_('Requerido. 15 caracteres ou menos. Letras, numeros e @/./+/-/_ characters'),validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])

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



    #Campos que ja vem com o User do Django
    first_name = models.CharField(_('Nome'), max_length=30, null=True) #nao ta como campo necessario
    last_name = models.CharField(_('Sobrenome'), max_length=30, null=True) #nao ta como campo necessario

    email = models.EmailField(verbose_name='E-mail', max_length=45, null=True, unique=True) #Changed: CharField to EmailField

    #USERNAME = NOME COMPLETO // INTERPRETAÇÃO: NOME DE USUARIO COMO SENDO NICKNAME, IDEIA É EXCLUIR O SHOW_NAME E UTILIZAR FIRST NAME E LAST NAME
    username =  models.CharField(verbose_name='Username',max_length=60, unique=True, help_text=_('Requerido. 15 caracteres ou menos. Letras, números e os seguintes caracteres: @/./+/-/_ '),validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Insira um username valido.'), _('invalido'))])
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    #campo que irá verificar se o usuário confirmou o Email
    is_trusty = models.BooleanField(_('trusty'), default=False, help_text=_('Diz se o usuário confirmou essa conta.'))

    def __str__(self):
        return self.username


    #algumas mudanças
    USERNAME_FIELD = 'username' #escolhendo a forma de login como sendo o username
    #campos necessários, são os que são necessários pra cadastro
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name','phone', 'street', 'house_number',
              'complement', 'district', 'CEP', 'CPF', 'link', 'profile_picture')

    #UserManager
    objects = UserManager()

    #Coisas que ja vem de base
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


#criando receptor para atualizar um usuário criado
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if(created):
#         User.objects.create(user=instance)
#     instance.user.save()
