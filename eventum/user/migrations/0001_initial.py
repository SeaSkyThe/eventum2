# Generated by Django 3.1.5 on 2021-01-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=45)),
                ('show_name', models.CharField(max_length=60, null=True)),
                ('email', models.CharField(max_length=45, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('house_number', models.IntegerField(null=True)),
                ('complement', models.CharField(max_length=255, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('CEP', models.CharField(max_length=20, null=True)),
                ('CPF', models.CharField(max_length=12, null=True)),
                ('active', models.BooleanField(default=True, null=True)),
                ('type_organizer', models.BooleanField(default=False, null=True)),
                ('type_participant', models.BooleanField(default=False, null=True)),
                ('link', models.CharField(max_length=255, null=True)),
                ('profile_picture', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
