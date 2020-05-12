# Generated by Django 3.0.5 on 2020-05-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_requirement'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='requirements',
            field=models.ManyToManyField(related_name='volunteers', to='categories.Requirement'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='help_types',
            field=models.ManyToManyField(related_name='volunteers', to='categories.HelpType'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='wards',
            field=models.ManyToManyField(blank=True, related_name='volunteers', to='categories.Ward'),
        ),
    ]
