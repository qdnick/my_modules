# from odoo.tests.common import TransactionCase
# from odoo import exceptions


# class TestHospitalModule(TransactionCase):

#     def setUp(self):
#         super(TestHospitalModule, self).setUp()
#         # Створення тестових даних
#         self.doctor = self.env["hr_hospital.doctor"].create(
#             {
#                 "name": "Dr. Test",
#                 "specialty_id": self.env.ref("hr_hospital.specialty_Oncologist").id,
#             }
#         )

#         self.patient = self.env["hr_hospital.patient"].create(
#             {"name": "John Doe", "age": 30, "doctor_id": self.doctor.id}
#         )

# def test_last_visit_method(self):
#     """Тест для перевірки методу отримання останнього візиту пацієнта до лікаря"""
#     # Створюємо візит
#     visit = self.env["hr_hospital.visit"].create(
#         {
#             "patient_id": self.patient.id,
#             "doctor_id": self.doctor.id,
#             "actual_date": "2023-10-14",
#             "status": "scheduled",
#         }
#     )
#     # Виклик методу last_visit
#     last_visit = self.patient.get_last_visit(self.doctor)
#     self.assertEqual(
#         last_visit.status, "scheduled", "Статус останнього візиту не співпадає"
#     )

# def test_is_intern_method(self):
#     """Тест для перевірки методу is_intern у моделі 'Doctor'"""
#     self.doctor.is_intern = True
#     self.assertTrue(self.doctor.is_intern, "Лікар повинен бути інтерном")

# def test_specialty_method(self):
#     """Тест для перевірки спеціальності лікаря"""
#     self.assertEqual(
#         self.doctor.specialty_id.name,
#         "Oncologist",
#         "Спеціальність повинна бути 'Oncologist'",
#     )
