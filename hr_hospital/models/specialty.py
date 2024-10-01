"""
Module specialty for hr_hospital

"""


from odoo import models, fields


class Specialty(models.Model):
    """
    Model Specialty.
    """

    _name = 'hr_hospital.specialty'
    _description = 'Hr_hospital Specialty'

    name = fields.Char(required=True,
                       translate=True)

    description = fields.Text(translate=True)
