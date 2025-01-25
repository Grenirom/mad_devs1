from faker import Faker

from tests.factories.base_factory import BaseUserFactory

fake = Faker()

class UserFactory(BaseUserFactory):
    role = 'user'

    @staticmethod
    def generate_user_data():
        return {
            'username': fake.user_name(),
            'role': 'user',
            'password': 'password123'
        }
