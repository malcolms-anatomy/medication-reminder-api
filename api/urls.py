from django.urls import path
from . import views

urlpatterns = [
    path('medication/', views.MedicationReminderListCreate.as_view(), name='medication-list-create'),
    path('medication/<int:pk>/', views.MedicationReminderDetail.as_view(), name='medication-detail'),
]
