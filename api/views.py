from rest_framework import generics
from .models import MedicationReminder
from .serializers import MedicationReminderSerializer

# View to get all reminders or create a new one
class MedicationReminderListCreate(generics.ListCreateAPIView):
    queryset = MedicationReminder.objects.all()
    serializer_class = MedicationReminderSerializer

# View to retrieve, update, or delete a specific reminder
class MedicationReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicationReminder.objects.all()
    serializer_class = MedicationReminderSerializer
