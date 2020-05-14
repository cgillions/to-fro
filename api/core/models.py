from django.contrib.auth import get_user_model
from django.db import models
from users.models import Coordinator, Resident, Volunteer, Person
from actions.models import Action


# Load our custom User model through Django.
User = get_user_model()


class NotificationTypes:
    """
    The available notification types that can be sent.

    Each of the types's value will be matched to a 
    `notifications/<value_in_lowercase>_{subject,message}.txt`
    template for generating the subject and message of the email
    """
    PENDING_HIGH_PRIORITY = 'PENDING_HIGH_PRIORITY'
    VOLUNTEER_INTEREST = 'VOLUNTEER_INTEREST'
    VOLUNTEER_ASSIGNED = 'VOLUNTEER_ASSIGNED'
    ACTION_COMPLETED = 'ACTION_COMPLETED'
    ACTION_NOT_COMPLETED = 'ACTION_NOT_COMPLETED'
    TYPES = (
        (PENDING_HIGH_PRIORITY, 'High priority action is pending'),
        (VOLUNTEER_INTEREST, 'Volunteed manifested interest'),
        (VOLUNTEER_ASSIGNED, 'Volunteer was assigned'),
        (ACTION_COMPLETED, 'Volunteer completed the action'),
        (ACTION_NOT_COMPLETED, 'Volunteer could not complete the action')
    )


class Notification(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True,
                            editable=False, choices=NotificationTypes.TYPES)
    action = models.ForeignKey(Action, null=True, on_delete=models.PROTECT,
                               help_text="The action the notification is about.")
    subject = models.CharField(
        max_length=100, null=True, help_text="The notification subject.")
    message = models.TextField(
        max_length=1000, null=True, help_text="What's your name?")
    delivered = models.BooleanField(
        default=False, help_text="This field is updated automatically.")
    sent_by = models.CharField(
        max_length=50, help_text="Who's sending the notification?")
    recipients = models.ManyToManyField(
        Person, related_name='notificationrecipient', default=list, help_text="This field is updated automatically.")
    created_date_time = models.DateTimeField(
        null=True, help_text="This field is updated automatically.")
    delivered_date_time = models.DateTimeField(
        null=True, help_text="This field is updated automatically.")
