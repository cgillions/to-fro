# Generated by Django 3.0.5 on 2020-05-04 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpType',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('private_description_template', models.TextField(
                    blank=True, help_text='Private description will be pre-filled with this text when picking this type of help for a Job', null=True)),
                ('public_description_template', models.TextField(
                    blank=True, help_text='Public description will be pre-filled with this text when picking this type of help for a Job', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(
                    blank=True, help_text='Main phone number for the user.', max_length=15, null=True)),
                ('phone_secondary', models.CharField(
                    blank=True, help_text='Secondary phone number for the user.', max_length=15, null=True)),
                ('email', models.CharField(
                    blank=True, help_text='Main email for the user.', max_length=50, null=True)),
                ('email_secondary', models.CharField(
                    blank=True, help_text='Secondary email for the user.', max_length=50, null=True)),
                ('notes', models.TextField(blank=True,
                                           help_text='Any other notes?', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                    parent_link=True, primary_key=True, serialize=False, to='users.Person')),
            ],
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                    parent_link=True, primary_key=True, serialize=False, to='users.Person')),
                ('dbs_number', models.CharField(
                    blank=True, help_text="The user's DBS certificate number, if they have one.", max_length=12, null=True)),
                ('access_to_car', models.BooleanField(
                    null=True, verbose_name='Has access to car')),
                ('driving_license', models.BooleanField(
                    null=True, verbose_name='Has a driving license')),
                ('ts_and_cs_confirmed', models.BooleanField(null=True,
                                                            verbose_name='Has agreed to terms and conditions')),
                ('health_checklist_received', models.BooleanField(
                    null=True, verbose_name='Has received their health checklist')),
                ('key_worker', models.BooleanField(null=True,
                                                   verbose_name='Has received key worker letter from council')),
                ('id_received', models.BooleanField(null=True,
                                                    verbose_name='Has sent a copy of their ID')),
                ('reference_details', models.CharField(
                    blank=True, max_length=250, null=True)),
                ('available_mon_morning', models.BooleanField(
                    default=False, verbose_name='Monday morning')),
                ('available_mon_afternoon', models.BooleanField(
                    default=False, verbose_name='Monday afternoon')),
                ('available_mon_evening', models.BooleanField(
                    default=False, verbose_name='Monday evening')),
                ('available_tues_morning', models.BooleanField(
                    default=False, verbose_name='Tuesday morning')),
                ('available_tues_afternoon', models.BooleanField(
                    default=False, verbose_name='Tuesday afternoon')),
                ('available_tues_evening', models.BooleanField(
                    default=False, verbose_name='Tuesday evening')),
                ('available_wed_morning', models.BooleanField(
                    default=False, verbose_name='Wednesday morning')),
                ('available_wed_afternoon', models.BooleanField(
                    default=False, verbose_name='Wednesday afternoon')),
                ('available_wed_evening', models.BooleanField(
                    default=False, verbose_name='Wednesday evening')),
                ('available_thur_morning', models.BooleanField(
                    default=False, verbose_name='Thursday morning')),
                ('available_thur_afternoon', models.BooleanField(
                    default=False, verbose_name='Thursday afternoon')),
                ('available_thur_evening', models.BooleanField(
                    default=False, verbose_name='Thursday evening')),
                ('available_fri_morning', models.BooleanField(
                    default=False, verbose_name='Friday morning')),
                ('available_fri_afternoon', models.BooleanField(
                    default=False, verbose_name='Friday afternoon')),
                ('available_fri_evening', models.BooleanField(
                    default=False, verbose_name='Friday evening')),
                ('available_sat_morning', models.BooleanField(
                    default=False, verbose_name='Saturday morning')),
                ('available_sat_afternoon', models.BooleanField(
                    default=False, verbose_name='Saturday afternoon')),
                ('available_sat_evening', models.BooleanField(
                    default=False, verbose_name='Saturday evening')),
                ('available_sun_morning', models.BooleanField(
                    default=False, verbose_name='Sunday morning')),
                ('available_sun_afternoon', models.BooleanField(
                    default=False, verbose_name='Sunday afternoon')),
                ('available_sun_evening', models.BooleanField(
                    default=False, verbose_name='Sunday evening')),
                ('help_types', models.ManyToManyField(
                    related_name='volunteer_help_types', to='users.HelpType')),
                ('wards', models.ManyToManyField(blank=True,
                                                 related_name='volunteer_wards', to='users.Ward')),
            ],
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                    parent_link=True, primary_key=True, serialize=False, to='users.Person')),
                ('address_line_1', models.CharField(
                    help_text='First line of their address.', max_length=100)),
                ('address_line_2', models.CharField(
                    blank=True, help_text='Second line of their address.', max_length=100, null=True)),
                ('address_line_3', models.CharField(
                    blank=True, help_text='Third line of their address.', max_length=100, null=True)),
                ('postcode', models.CharField(
                    help_text='Address postcode.', max_length=10)),
                ('internet_access', models.BooleanField(default=False,
                                                        help_text='Does this person have internet access?')),
                ('smart_device', models.BooleanField(default=False,
                                                     help_text='Does this person have a smart device?')),
                ('confident_online_shopping', models.BooleanField(
                    default=False, help_text='Is this person confident online shopping?')),
                ('confident_online_comms', models.BooleanField(default=False,
                                                               help_text='Is this person confident communicating online?')),
                ('shielded', models.BooleanField(
                    default=False, help_text='Is this person shielded?')),
                ('ward', models.ForeignKey(help_text='The ward containing the above address.',
                                           null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Ward')),
            ],
            bases=('users.person',),
        ),
    ]
