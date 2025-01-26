
from rest_framework import status
from django.contrib.auth import get_user_model
from src.patients.models import Patient
from tests.factories.doctor_factory import DoctorFactory
from tests.factories.user_factory import UserFactory
from tests.test_core.test_base_class import BaseTest

User = get_user_model()


class PatientsAPITest(BaseTest):
    def setUp(self):
        # создаем 2 пациента для тестов листинга
        self.patient1 = Patient.objects.create(date_of_birth="1990-01-01", diagnoses=["test1"])
        self.patient2 = Patient.objects.create(date_of_birth="1985-05-15", diagnoses=["test2", "test3"])

    def test_access_for_doctor(self):
        """Доктор должен иметь доступ к списку пациентов"""
        self.client.force_authenticate(user=self.default_doctor)
        response = self.client.get(self.patients_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Убедимся, что видим все записи пациентов

    def test_access_for_non_doctor(self):
        """Пользователи без роли 'doctor' не должны иметь доступ"""
        self.client.force_authenticate(user=self.default_user)
        response = self.client.get(self.patients_url)
        self.assertEqual(response.status_code, 403)

    def test_access_for_anonymous_user(self):
        """Анонимный пользователь не должен иметь доступ"""
        response = self.client.get(self.patients_url)
        self.assertEqual(response.status_code, 401)