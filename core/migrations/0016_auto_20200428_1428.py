# Generated by Django 3.0.5 on 2020-04-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_merge_20200428_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='access_to_car',
            field=models.BooleanField(null=True, verbose_name='Has access to car'),
        ),
        migrations.AlterField(
            model_name='helper',
            name='available_sat_morning',
            field=models.BooleanField(default=False, verbose_name='Saturday morning'),
        ),
        migrations.AlterField(
            model_name='helper',
            name='driving_license',
            field=models.BooleanField(null=True, verbose_name='Has a driving license'),
        ),
        migrations.AlterField(
            model_name='helper',
            name='health_checklist_received',
            field=models.BooleanField(null=True, verbose_name='Has received their health checklist'),
        ),
        migrations.AlterField(
            model_name='helper',
            name='id_received',
            field=models.BooleanField(null=True, verbose_name='Has sent a copy of their ID'),
        ),
        migrations.AlterField(
            model_name='helper',
            name='key_worker',
            field=models.BooleanField(null=True, verbose_name='Has received key worker letter from council'),
        ),
        migrations.AlterField(
            model_name='helper',
            name='ts_and_cs_confirmed',
            field=models.BooleanField(null=True, verbose_name='Has agreed to terms and conditions'),
        ),
        migrations.CreateModel(
            name='HelpPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help_type', models.ForeignKey(help_text="The type of help they're happy to do.", null=True, on_delete=django.db.models.deletion.PROTECT, to='core.HelpType')),
                ('helper', models.ForeignKey(help_text='The associated user.', null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Helper')),
            ],
        ),
    ]
