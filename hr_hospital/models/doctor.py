"""
Module doctor for hr_hospital

"""

import logging

from odoo import models, fields, api


_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    """
    Represents a doctor in the hospital system.

    This class contains the necessary fields
    and methods to manage doctor-related
    data, such as their specialty, patients,
    and mentorship details.

    Attributes:
        name (str): Full name of the doctor.
        specialty_id (Many2one): Reference to the doctor's specialty.
        intern_ids (One2many): List of interns mentored by the doctor.
        patient_ids (One2many): List of patients assigned to the doctor.
    """

    _name = "hr_hospital.doctor"
    _inherit = "hr_hospital.person"
    _description = "Hr_hospital Doctor"

    specialty_id = fields.Many2one("hr_hospital.specialty", string="Specialty")
    is_intern = fields.Boolean(string="Intern")
    mentor_id = fields.Many2one(
        "hr_hospital.doctor",
        string="Doctor-mentor",
        domain="[('is_intern', '=', False)]",
    )

    patient_ids = fields.One2many(
        "hr_hospital.patient",
        "personal_doctor_id",
        string="Patients",
    )
    # added intern/mentor
    intern_ids = fields.One2many(
        "hr_hospital.doctor",
        "mentor_id",
        string="Interns",
    )

    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        readonly=False,
        default=lambda self: self.env.company,
    )

    visit_ids = fields.One2many(
        "hr_hospital.visit",
        "doctor_id",
        string="Visits",
    )

    # debug
    def doctor_debug_report(self):
        return "1_1_doctor"

    # ---
    # add file link for report
    def _get_report_base_filename(self):
        self.ensure_one()
        return "Hr hospital - %s" % (self.display_name)

    def action_create_visit(self):
        # fast creat visit
        _logger.info(self.id)

        return {
            "type": "ir.actions.act_window",
            "name": "Create Visit",
            "res_model": "hr_hospital.visit",
            "view_mode": "form",
            "context": {
                "default_doctor_id": self.id,
            },
            "target": "new",
        }

    # ---
    @api.onchange("is_intern")
    def _onchange_is_intern(self):
        if not self.is_intern:
            self.mentor_id = False

    @api.depends("res_model", "res_id")
    def _compute_resource_ref(self):
        for rec in self:
            if rec.res_model and rec.res_model in self.env:
                rec.resource_ref = "%s,%s" % (rec.res_model, rec.res_id or 0)
            else:
                rec.resource_ref = None

    # clear mentor
    def action_remove_promo(self):

        self.ensure_one()
        self.promo_ids = [(5, 0, 0)]
