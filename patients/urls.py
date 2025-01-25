from django.urls import path

from patients.views import LoginView, PatientsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('patients/', PatientsView.as_view(), name='patients')
]