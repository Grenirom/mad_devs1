from django.urls import path

from src.patients.views import PatientsView

urlpatterns = [
    path('patients/', PatientsView.as_view(), name='patients')
]