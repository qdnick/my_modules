from odoo import models, fields


class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Patient Visit'

    patient_id = fields.Many2one(
        'hr_hospital.patient', string='Patient')
    date = fields.Date(string='Visit Date', required=True)
    notes = fields.Text(string='Notes')
