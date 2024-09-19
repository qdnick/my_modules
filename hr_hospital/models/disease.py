"""
Module disease for hr_hospital

"""


from odoo import models, fields


class Disease(models.Model):
    """
    Model Disease.
    """
    
    _name = 'hr_hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
