"""
Module patient for hr_hospital

"""

from odoo import models, fields, api


class Patient(models.Model):
    """
    Model Patient.
    """

    _name = "hr_hospital.patient"

    _inherit = "hr_hospital.person"
    _description = "Hr_hospital Patient"

    personal_doctor_id = fields.Many2one(
        "hr_hospital.doctor",
        string="Personal Doctor",
    )

    birth_date = fields.Date()
    passport_info = fields.Char()
    contact_person = fields.Char()

    age = fields.Integer(compute="_compute_age")

    visit_ids = fields.One2many(
        "hr_hospital.visit",
        "patient_id",
        string="Visit History",
    )

    diagnosis_ids = fields.One2many(
        "hr_hospital.diagnosis",
        compute="_compute_diagnosis_ids",
        string="Diagnosis History",
    )

    # debug
    def patient_debug_report(self):
        return "1_1_patient"

    def get_last_visit_status(self, doctor_id):
        # find last visit status
        last_visit = self.env["hr_hospital.visit"].search(
            [("patient_id", "=", self.id), ("doctor_id", "=", doctor_id)],
            order="actual_date desc",
            limit=1,
        )

        if last_visit:
            return last_visit.status
        return False

    # ---

    @api.depends("visit_ids")
    def _compute_diagnosis_ids(self):
        for patient in self:
            # get all patients visits
            visits = patient.visit_ids
            # visits-> diagnoses
            diagnoses = self.env["hr_hospital.diagnosis"].search(
                [("visit_id", "in", visits.ids)]
            )
            patient.diagnosis_ids = diagnoses

    def open_patient_visits(self):
        # """Method to open the patient's visits
        return {
            "type": "ir.actions.act_window",
            "name": "Visits",
            "view_mode": "tree,form",
            "res_model": "hr_hospital.visit",
            "domain": [("patient_id", "=", self.id)],
            "context": {"default_patient_id": self.id},
        }

    def quick_visit(self):
        # Method to create a quick visit
        return {
            "type": "ir.actions.act_window",
            "name": "Quick Visit",
            "view_mode": "form",
            "res_model": "hr_hospital.visit",
            "context": {
                "default_patient_id": self.id,
                "default_doctor_id": self.personal_doctor_id.id,
            },
            "target": "new",
        }

    @api.depends("birth_date")
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                patient.age = fields.Date.today().year - patient.birth_date.year
            else:
                patient.age = 0
