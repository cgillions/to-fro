# Generated by Django 3.0.5 on 2020-04-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200426_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='wards',
            field=models.ManyToManyField(
                related_name='helpers', to='core.Ward'),
        ),
    ]
