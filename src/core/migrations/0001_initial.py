# Generated by Django 3.0.5 on 2020-05-11 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='The notification subject.', max_length=100, null=True)),
                ('message', models.TextField(help_text="What's your name?", max_length=1000, null=True)),
                ('delivered', models.BooleanField(default=False, help_text='This field is updated automatically.')),
                ('sent_by', models.CharField(help_text="Who's sending the notification?", max_length=50)),
                ('created_date_time', models.DateTimeField(help_text='This field is updated automatically.', null=True)),
                ('delivered_date_time', models.DateTimeField(help_text='This field is updated automatically.', null=True)),
                ('action', models.ForeignKey(help_text='The action the notification is about.', null=True, on_delete=django.db.models.deletion.PROTECT, to='actions.Action')),
                ('recipients', models.ManyToManyField(default=list, help_text='This field is updated automatically.', related_name='notificationrecipient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]