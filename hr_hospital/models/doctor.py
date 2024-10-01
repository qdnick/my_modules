"""
Module doctor for hr_hospital

"""


from odoo import models, fields, api


class Doctor(models.Model):
    """
    Model Doctor.
    """

    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Hr_hospital Doctor'

    specialty_id = fields.Many2one('hr_hospital.specialty',
                                   string='Specialty')
    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one('hr_hospital.doctor',
                                string='Doctor-mentor',
                                domain="[('is_intern', '=', False)]")

    patient_ids = fields.One2many('hr_hospital.patient',
                                  'personal_doctor_id',
                                  string='Patients')

    @api.onchange('is_intern')
    def _onchange_is_intern(self):
        if not self.is_intern:
            self.mentor_id = False

    @api.depends('res_model', 'res_id')
    def _compute_resource_ref(self):
        for rec in self:
            if rec.res_model and rec.res_model in self.env:
                rec.resource_ref = '%s,%s' % (
                    rec.res_model, rec.res_id or 0)
            else:
                rec.resource_ref = None

    # clear mentor
    def action_remove_promo(self):

        self.ensure_one()
        self.promo_ids = [(5, 0, 0)]
