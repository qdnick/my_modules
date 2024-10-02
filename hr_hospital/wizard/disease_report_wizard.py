"""
This wizard for constract report
"""


from odoo import models, fields, api


class DiseaseReportWizard(models.TransientModel):
    # search elements

    _name = 'disease.report.wizard'
    _description = 'Wizard for Disease Report'

    doctor_ids = fields.Many2many(
        'hr_hospital.doctor',
        string="Doctors")
    disease_ids = fields.Many2many(
        'hr_hospital.disease',
        string="Diseases")
    date_from = fields.Date(string="From")
    date_to = fields.Date(string="To")

    def generate_report(self):
        domain = []

        # Doc filter
        if self.doctor_ids:
            domain.append(('visit_id.doctor_id', 'in', self.doctor_ids.ids))

        # Disease filter
        if self.disease_ids:
            domain.append(('disease_id', 'in', self.disease_ids.ids))

        # Date filter
        if self.date_from:
            domain.append(('visit_id.actual_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('visit_id.actual_date', '<=', self.date_to))

        # diagnoses
        # diagnoses = self.env['hr_hospital.diagnosis'].search(domain)

        # action
        action = self.env["ir.actions.actions"]._for_xml_id(
            "hr_hospital.action_hr_hospital_diagnoses"
        )
        action.update({
            "domain": domain,
            "context": {'group_by': ['disease_id']},
        })
        return action

    # added docs in filter
    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        doc_ids = self.env['hr_hospital.doctor'].browse(
            self.env.context['active_ids'])
        res['doctor_ids'] = [(6, 0, doc_ids.ids)]
        return res
