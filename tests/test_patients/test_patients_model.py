from datetime import date

from src.patients.models import Patient

from tests.test_core.test_base_class import BaseTest


class PatientModelTest(BaseTest):
    def test_successful_create_patient(self):
        """Проверка успешного создания объекта Patient"""
        patient = Patient.objects.create(
            date_of_birth=date(1985, 5, 15),
            diagnoses=["test1", "test2"]
        )
        self.assertEqual(patient.date_of_birth.isoformat(), "1985-05-15")
        self.assertEqual(patient.diagnoses, ["test1", "test2"])
        self.assertIsNotNone(patient.created_at)


    def test_default_diagnoses(self):
        """Проверка значения diagnoses по умолчанию"""
        patient = Patient.objects.create(date_of_birth="1990-01-01")
        self.assertEqual(patient.diagnoses, [])