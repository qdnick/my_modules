"""
Module patient for hr_hospital

"""


from odoo import models, fields, api


class Patient(models.Model):
    """
    Model Patient.
    """

    _name = 'hr_hospital.patient'

    _inherit = 'hr_hospital.person'
    _description = 'Hr_hospital Patient'

    personal_doctor_id = fields.Many2one('hr_hospital.doctor',
                                         string='Personal Doctor')
    birth_date = fields.Date()
    passport_info = fields.Char()
    contact_person = fields.Char()

    age = fields.Integer(compute='_compute_age')

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                patient.age = \
                    (fields.Date.today().year - patient.birth_date.year)
            else:
                patient.age = 0
