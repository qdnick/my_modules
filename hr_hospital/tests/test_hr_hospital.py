"""
TransactionCase test

"""

from odoo.tests.common import TransactionCase

# from odoo import exceptions


class TestHospitalModule(TransactionCase):

    def setUp(self):
        super(TestHospitalModule, self).setUp()
        # Create mass data
        self.doctor = self.env["hr_hospital.doctor"].create(
            {
                "name": "Dr. Test",
                "specialty_id": self.env.ref("hr_hospital.specialty_Oncologist").id,
            }
        )

        self.patient = self.env["hr_hospital.patient"].create(
            {"name": "John Doe", "age": 30, "doctor_id": self.doctor.id}
        )


def test_last_visit_method(self):
    """The last vicit test"""

    # create visit
    visit = self.env["hr_hospital.visit"].create(
        {
            "patient_id": self.patient.id,
            "doctor_id": self.doctor.id,
            "actual_date": "2023-10-14",
            "status": "scheduled",
        }
    )
    self.assertTrue(visit.id, "Visit should be created successfully")

    # method last_visit
    last_visit = self.patient.get_last_visit(self.doctor)
    self.assertEqual(
        last_visit.status,
        "scheduled",
        "The status of the last visit does not match",
    )


def test_is_intern_method(self):
    """Itnern test"""
    self.doctor.is_intern = True
    self.assertTrue(
        self.doctor.is_intern,
        "The doctor must be intern",
    )


def test_specialty_method(self):
    """Specialty test"""
    self.assertEqual(
        self.doctor.specialty_id.name,
        "Oncologist",
        "The specialty must be 'Oncologist'",
    )
