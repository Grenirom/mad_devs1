from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics, permissions

from src.generals.permissions import IsDoctor

from src.patients.models import Patient
from src.patients.serializers import PatientSerializer


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny, ]


class PatientsView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctor,]
