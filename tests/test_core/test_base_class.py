from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

User = get_user_model()


class PatientTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.login_url = reverse('login')
        cls.patient_url = reverse('patients')

        cls.new_user = User.objects.create(
            username='Doctor1',
            role='doctor',
            password='password123'
        )
        cls.login_existing_data = {'username': 'Doctor1', 'password': 'password123'}
        cls.login_invalid_data = {'username': 'wrong_username', 'password': 'wrong_password'}
