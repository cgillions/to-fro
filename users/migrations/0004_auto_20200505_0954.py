# Generated by Django 3.0.5 on 2020-05-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200504_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='user_without_account',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='user_without_account',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]