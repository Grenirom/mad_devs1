from tests.test_core.test_base_class import PatientTest


class LoginAPITest(PatientTest):
    def test_successful_login(self):
        required_fields_in_data = {'refresh', 'access'}
        response = self.client.post(self.login_url, data=self.login_existing_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(required_fields_in_data.issubset(response.data.keys()))

    def test_login_fail(self):
        response = self.client.post(self.login_url, data=self.login_invalid_data)
        self.assertEqual(response.status_code, 401)

    def test_login_empty_fields(self):
        empty_data = {'username': '',  'password': ''}
        response_fields = {'username', 'password'}
        response = self.client.post(self.login_url, data=empty_data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(response_fields.issubset(response.data.keys()))