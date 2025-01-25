from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import generics, permissions

from patients.models import Patient
from patients.permissions import IsDoctor
from patients.serializers import PatientSerializer


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny, ]


class PatientsView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctor,]
