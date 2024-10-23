"""update doctor in patients"""

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MassUpdateDoctorWizard(models.TransientModel):
    """
    Wizard for reassigning the personal doctor of a patient.

    This wizard allows the user to select a new doctor and reassign
    the personal doctor of a specific patient.

    Attributes:
        patient_id (Many2one): The patient whose doctor is being reassigned.
        new_doctor_id (Many2one): The new doctor to assign to the patient.
    """

    _name = "mass.update.doctor.wizard"
    _description = "Wizard for mass updating personal doctors for patients"

    new_doctor_id = fields.Many2one(
        "hr_hospital.doctor", string="New Personal Doctor", required=True
    )

    @api.model
    def default_get(self, fields_list):

        res = super(MassUpdateDoctorWizard, self).default_get(fields_list)
        active_ids = self.env.context.get("active_ids")

        if not active_ids:
            raise UserError(_("No patients selected."))
        return res

    def action_update_doctor(self):
        active_ids = self.env.context.get("active_ids")

        if not active_ids:
            raise UserError(_("No patients selected."))

        patients = self.env["hr_hospital.patient"].browse(active_ids)
        for patient in patients:
            patient.personal_doctor_id = self.new_doctor_id
