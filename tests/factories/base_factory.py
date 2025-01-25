import factory
from faker import Faker
from src.users.models import User

fake = Faker()

class BaseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.user_name())
    password = factory.PostGenerationMethodCall('set_password', 'password123')
