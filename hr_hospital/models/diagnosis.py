"""
Module diagnosis    for hr_hospital

"""

from odoo import models, fields


class Diagnosis(models.Model):
    """
    Model Diagnosis
    """

    _name = "hr_hospital.diagnosis"
    _description = "Diagnosis"

    visit_id = fields.Many2one("hr_hospital.visit", required=True)
    disease_id = fields.Many2one("hr_hospital.disease", required=True)
    description = fields.Text()
    approved = fields.Boolean(string="Approved by Mentor")

    # added visit actual date
    visit_actual_date = fields.Date(
        related="visit_id.actual_date_day", store=True, string="Visit Date"
    )
