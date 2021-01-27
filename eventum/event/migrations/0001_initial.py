# Generated by Django 3.1.5 on 2021-01-21 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('activity_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organize_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('cost', models.FloatField()),
                ('description', models.CharField(max_length=255, null=True)),
                ('subscription_limit', models.IntegerField(null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.event')),
            ],
        ),
    ]