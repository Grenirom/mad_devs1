from django.core.exceptions import ValidationError
from django.db import IntegrityError

from src.users.models import User
from tests.factories.user_factory import UserFactory
from tests.test_core.test_base_class import BaseTest


class UserModelTest(BaseTest):
    def test_password_hash_on_creation(self):
        user_data = UserFactory.generate_user_data()
        user = User.objects.create(**user_data)
        self.assertNotEqual(user.password, user_data.get('password'))
        self.assertTrue(user.password.startswith('pbkdf2_'))

    def test_password_not_rehashed_on_update(self):
        user = self.default_user
        old_password_hash = user.password
        user.username = 'new_username'
        user.save()
        print(user.password)
        print(old_password_hash)   # хеш пароля не должен обновляться при обновлении данных пользователя
        self.assertEqual(user.password, old_password_hash)

    def test_invalid_role(self):
        with self.assertRaises(ValidationError):
            user = UserFactory.create(role='invalid')
            user.full_clean()    # Запускает проверку поля role на соответствие choices

    def test_duplicate_username(self):
        """проверяет вызовется лли IntegrityError если продублировать username"""
        user_data = UserFactory.generate_user_data()
        User.objects.create(**user_data)
        with self.assertRaises(IntegrityError):
            User.objects.create(**user_data)

    def test_superuser_creation(self):
        """Проверяет что при создании суперюзера поля is_staff is_superuser выставляются правильно"""
        superuser = User.objects.create_superuser(username='admin', password='admin_password', role='user')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)