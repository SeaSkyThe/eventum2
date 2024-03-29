# Generated by Django 3.1.6 on 2021-02-17 01:05

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210216_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city',
            new_name='district',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', help_text='Requerido. 15 caracteres ou menos. Letras, numeros e @/./+/-/_ characters', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='Nome de usuário'),
        ),
    ]
