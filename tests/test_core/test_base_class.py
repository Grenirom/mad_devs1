from django.urls import reverse
from src.users.models import User

from rest_framework.test import APITestCase

from tests.factories.doctor_factory import DoctorFactory
from tests.factories.user_factory import UserFactory


class BaseTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.login_url = reverse('login')

        cls.default_user = UserFactory.create()
        cls.default_doctor = DoctorFactory.create()
