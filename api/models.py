from django.db import models

class MedicationReminder(models.Model):
    user_email = models.EmailField()
    medication_name = models.CharField(max_length=255)
    dose = models.CharField(max_length=50)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication_name} for {self.user_email}"
