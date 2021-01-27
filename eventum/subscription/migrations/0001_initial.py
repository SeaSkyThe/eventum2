# Generated by Django 3.1.5 on 2021-01-21 14:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cost', models.FloatField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.activity')),
                ('subscription_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subscription.subscription')),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subscription.subscription_type'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user'),
        ),
    ]
