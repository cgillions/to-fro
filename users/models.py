from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager
from django.utils import timezone
from django.db import models


class Ward(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.name}"


class HelpType(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.name}"


class UserRole:
    '''Constants used in the User class.'''
    COORDINATOR, REQUESTER, VOLUNTEER = '1', '2', '3'
    ROLES = [
        (COORDINATOR, "Coordinator"),
        (REQUESTER, "Requester"),
        (VOLUNTEER, "Volunteer")
    ]


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom Base User class.
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model
    '''
    # Constants used by Django.
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']
    
    # Default User attributes.
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    # Custom User attributes.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=UserRole.ROLES, help_text="The role of the user.")
    phone = models.CharField(max_length=15, null=True, blank=True, help_text="Main phone number for the user.")
    phone_secondary = models.CharField(max_length=15, null=True, blank=True, help_text="Secondary phone number for the user.")
    email = models.CharField(max_length=50, null=True, blank=True, help_text="Main email for the user.")
    email_secondary = models.CharField(max_length=50, null=True, blank=True, help_text="Secondary email for the user.")
    notes = models.CharField(max_length=500, null=True, blank=True, help_text="Any other notes?")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.username


class Requester(User):
    address_line_1 = models.CharField(max_length=100, help_text="First line of their address.")
    address_line_2 = models.CharField(max_length=100, null=True, blank=True, help_text="Second line of their address.")
    address_line_3 = models.CharField(max_length=100, null=True, blank=True, help_text="Third line of their address.")
    postcode = models.CharField(max_length=10, help_text="Address postcode.")
    ward = models.ForeignKey(Ward, null=True, on_delete=models.PROTECT, help_text="The ward containing the above address.")
    internet_access = models.BooleanField(default=False, help_text="Does this person have internet access?")
    smart_device = models.BooleanField(default=False, help_text="Does this person have a smart device?")
    confident_online_shopping = models.BooleanField(default=False, help_text="Is this person confident online shopping?")
    confident_online_comms = models.BooleanField(default=False, help_text="Is this person confident communicating online?")
    shielded = models.BooleanField(default=False, help_text="Is this person shielded?")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        

class Volunteer(User):
    dbs_number = models.CharField(max_length=12, null=True, blank=True, help_text="The user's DBS certificate number, if they have one.")
    access_to_car = models.BooleanField(null=True, verbose_name="Has access to car")
    driving_license = models.BooleanField(null=True, verbose_name="Has a driving license")
    ts_and_cs_confirmed = models.BooleanField(null=True, verbose_name="Has agreed to terms and conditions")
    health_checklist_received = models.BooleanField(null=True, verbose_name="Has received their health checklist")
    key_worker = models.BooleanField(null=True, verbose_name="Has received key worker letter from council")
    id_received = models.BooleanField(null=True, verbose_name="Has sent a copy of their ID")
    wards = models.ManyToManyField(Ward, blank=True, related_name="volunteer_wards")
    help_types = models.ManyToManyField(HelpType, related_name="volunteer_help_types")
    reference_details = models.CharField(max_length=250, null=True, blank=True)
    available_mon_morning = models.BooleanField(default=False, verbose_name="Monday morning")
    available_mon_afternoon = models.BooleanField(default=False, verbose_name="Monday afternoon")
    available_mon_evening = models.BooleanField(default=False, verbose_name="Monday evening")
    available_tues_morning = models.BooleanField(default=False, verbose_name="Tuesday morning")
    available_tues_afternoon = models.BooleanField(default=False, verbose_name="Tuesday afternoon")
    available_tues_evening = models.BooleanField(default=False, verbose_name="Tuesday evening")
    available_wed_morning = models.BooleanField(default=False, verbose_name="Wednesday morning")
    available_wed_afternoon = models.BooleanField(default=False, verbose_name="Wednesday afternoon")
    available_wed_evening = models.BooleanField(default=False, verbose_name="Wednesday evening")
    available_thur_morning = models.BooleanField(default=False, verbose_name="Thursday morning")
    available_thur_afternoon = models.BooleanField(default=False, verbose_name="Thursday afternoon")
    available_thur_evening = models.BooleanField(default=False, verbose_name="Thursday evening")
    available_fri_morning = models.BooleanField(default=False, verbose_name="Friday morning")
    available_fri_afternoon = models.BooleanField(default=False, verbose_name="Friday afternoon")
    available_fri_evening = models.BooleanField(default=False, verbose_name="Friday evening")
    available_sat_morning = models.BooleanField(default=False, verbose_name="Saturday morning")
    available_sat_afternoon = models.BooleanField(default=False, verbose_name="Saturday afternoon")
    available_sat_evening = models.BooleanField(default=False, verbose_name="Saturday evening")
    available_sun_morning = models.BooleanField(default=False, verbose_name="Sunday morning")
    available_sun_afternoon = models.BooleanField(default=False, verbose_name="Sunday afternoon")
    available_sun_evening = models.BooleanField(default=False, verbose_name="Sunday evening")
    
    def __str__(self):
        return self.full_name


# class Relationship(models.Model):
#     user_1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_1")
#     user_2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_2")
#     created_datetime = models.DateTimeField(default=timezone.now, help_text="When did they first make contact?")
    
#     def __str__(self):
#         return f"{self.id}: {self.user_1} and {self.user_2}"
