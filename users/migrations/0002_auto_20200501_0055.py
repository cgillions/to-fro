# Generated by Django 3.0.5 on 2020-05-01 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requester',
            name='ward',
            field=models.ForeignKey(help_text='The ward containing the above address.', null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Ward'),
        ),
    ]
