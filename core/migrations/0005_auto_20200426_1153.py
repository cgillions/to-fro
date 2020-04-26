# Generated by Django 3.0.5 on 2020-04-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_set_default_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requester',
            name='address_line_2',
            field=models.CharField(blank=True, help_text='Second line of their address.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='requester',
            name='address_line_3',
            field=models.CharField(blank=True, help_text='Third line of their address.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='requester',
            name='user_type',
            field=models.CharField(blank=True, default='requester', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_primary',
            field=models.CharField(blank=True, help_text='Main email for the user.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_secondary',
            field=models.CharField(blank=True, help_text='Secondary email for the user.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='notes',
            field=models.CharField(blank=True, help_text='Any other notes?', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number_secondary',
            field=models.CharField(blank=True, help_text='Secondary phone number for the user.', max_length=15, null=True),
        ),
    ]