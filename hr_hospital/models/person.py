"""
Module person for hr_hospital

"""

from odoo import models, fields, api


class Person(models.AbstractModel):
    """
    Model Person
    """

    _name = "hr_hospital.person"
    _description = "Abstract Person"

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    phone = fields.Char(string="Phone number")
    photo = fields.Image()
    gender = fields.Selection([("male", "Male"), ("female", "Female")])

    # add user id
    user_id = fields.Many2one(
        "res.users",
        string="User",
        help="The user related to this patient.",
    )

    @api.depends("last_name", "first_name")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.last_name or ""} {rec.first_name or ""}'
