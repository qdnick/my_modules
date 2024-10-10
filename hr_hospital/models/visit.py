"""
Module visit for hr_hospital

"""

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Visit(models.Model):
    """
    Model Visit.
    """

    _name = "hr_hospital.visit"
    _inherit = ["mail.thread"]
    _description = "Hr_hospital Visit"

    status = fields.Selection(
        [
            ("scheduled", "Scheduled"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        string="Visit Status",
        default="scheduled",
    )

    scheduled_date = fields.Datetime()
    actual_date = fields.Datetime()

    # scheduled_date_day
    scheduled_date_day = fields.Date(
        compute="_compute_scheduled_date",
        store=True,
        string="Scheduled Date (Only Day)",
    )
    actual_date_day = fields.Date(
        compute="_compute_actual_date",
        store=True,
        string="Actual Date (Only Day)",
    )

    @api.depends("actual_date")
    def _compute_actual_date(self):
        for rec in self:
            rec.actual_date_day = rec.actual_date.date() if rec.actual_date else False

    @api.depends("scheduled_date")
    def _compute_scheduled_date(self):
        for rec in self:
            rec.scheduled_date_day = (
                rec.scheduled_date.date() if rec.scheduled_date else False
            )

    doctor_id = fields.Many2one(
        "hr_hospital.doctor",
        string="Doctor",
        required=True,
    )

    patient_id = fields.Many2one(
        "hr_hospital.patient",
        string="Patient",
        required=True,
    )

    diagnosis_ids = fields.One2many(
        "hr_hospital.diagnosis",
        "visit_id",
        string="Diagnoses",
    )

    # completed visit
    @api.constrains("status", "scheduled_date", "doctor_id")
    def _check_completed_visit(self):
        for visit in self:
            if visit.status == "completed":
                raise ValidationError(
                    _("You cannot change the details " "of a completed visit.")
                )

    # block changes
    @api.constrains("status", "scheduled_date", "actual_date", "doctor_id")
    def _check_completed_visit(self):
        for visit in self:
            if visit.status == "completed":
                raise ValidationError(
                    _("You cannot change the details " "of a completed visit.")
                )

    @api.model
    def unlink(self):
        # block removal
        if any(visit.diagnosis_ids for visit in self):
            raise UserError(_("You cannot delete of a completed visit."))
        return super(Visit, self).unlink()

    def write(self, vals):
        # block deactivate
        if "active" in vals and not vals.get("active"):
            if any(visit.diagnosis_ids for visit in self):
                raise UserError(
                    _(
                        """You cannot deactivate "
                        "of a completed visit."""
                    )
                )
        return super(Visit, self).write(vals)

    @api.constrains("scheduled_date", "doctor_id", "patient_id")
    def _check_duplicate_visit(self):
        # check visits
        for visit in self:
            if visit.scheduled_date and visit.doctor_id and visit.patient_id:
                same_day_visits = self.search(
                    [
                        ("doctor_id", "=", visit.doctor_id.id),
                        ("patient_id", "=", visit.patient_id.id),
                        ("scheduled_date", "=", visit.scheduled_date.date()),
                        ("id", "!=", visit.id),
                    ]
                )
                if same_day_visits:
                    raise ValidationError(
                        _(
                            "You cannot make an appointment with "
                            "the same doctor more than once a day."
                        )
                    )
