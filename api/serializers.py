from rest_framework import serializers
from .models import MedicationReminder

class MedicationReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationReminder
        fields = ['id', 'user_email', 'medication_name', 'dose', 'time', 'created_at']
