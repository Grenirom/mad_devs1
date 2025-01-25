
from rest_framework import generics

from src.generals.permissions import IsDoctor

from src.patients.models import Patient
from src.patients.serializers import PatientSerializer


class PatientsView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctor,]
