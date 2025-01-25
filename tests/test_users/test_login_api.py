from tests.test_core.test_base_class import BaseTest


class LoginAPITest(BaseTest):
    def test_successful_login(self):
        required_fields_in_data = {'refresh', 'access'}
        successful_login_data = {'username': self.default_user.username, 'password': 'password123'}
        response = self.client.post(self.login_url, data=successful_login_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(required_fields_in_data.issubset(response.data.keys()))

    def test_login_fail(self):
        invalid_login_data = {'username': 'invalid_data', 'password': 'invalid_data'}
        response = self.client.post(self.login_url, data=invalid_login_data)
        self.assertEqual(response.status_code, 401)

    def test_login_empty_fields(self):
        empty_data = {'username': '',  'password': ''}
        response_fields = {'username', 'password'}
        response = self.client.post(self.login_url, data=empty_data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(response_fields.issubset(response.data.keys()))