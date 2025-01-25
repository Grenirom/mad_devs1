from tests.factories.base_factory import BaseUserFactory


class DoctorFactory(BaseUserFactory):
    role = 'doctor'