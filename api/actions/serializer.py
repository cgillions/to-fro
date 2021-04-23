from django.urls import path, include
from .models import Action
#from users.models import Volunteer
from rest_framework import serializers

# Serializers define the API representation.

'''
class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = [
            "id", "first_name", "last_name", "phone", "phone_secondary", "email", "notes",
            "external_volunteer_id", "wards", "help_types", "requirements",
        ]
'''

class ActionListSerializer(serializers.ModelSerializer):
    resident = serializers.StringRelatedField(many=False)
    help_type = serializers.StringRelatedField(many=False)
    action_status = serializers.CharField(source='get_action_status_display')

    class Meta:
        model = Action
        fields = [
            'pk', 'resident', 'help_type', 'requested_datetime', 'volunteer_made_contact_on',
            'action_status', 'time_taken'
        ]
        #depth = 1


class ActionSerializer(serializers.ModelSerializer):
    interested_volunteers = serializers.StringRelatedField(many=True)
    #assigned_volunteers = VolunteerSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = [
            'pk', 'resident', 'help_type', 'action_priority', 'requested_datetime',
            'volunteer_made_contact_on', 'coordinator', 'minimum_volunteers', 'maximum_volunteers',
            'requirements', 'external_action_id', 'public_description', 'private_description',
            'action_status', 'time_taken', 'added_by', 'call_datetime', 'call_duration',
            'assigned_volunteers', 'interested_volunteers', 'assigned_date', 'completed_date',
        ]
        depth = 1


