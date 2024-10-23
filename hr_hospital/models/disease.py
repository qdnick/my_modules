"""
Module disease for hr_hospital

"""

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Disease(models.Model):
    """
    Represents a disease in the hospital system.

    This class defines the structure for storing
    information about diseases.
    It also includes a hierarchy of diseases
    for more organized classification.

    Attributes:
        name (str):
            Name of the disease.
        parent_id (Many2one):
            Parent disease to create a hierarchy.
        child_ids (One2many):
            List of sub-diseases (children) under this disease.
    """

    _name = "hr_hospital.disease"
    _description = "Disease"
    _parent_name = "parent_id"

    description = fields.Text(translate=True)

    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = "complete_name"

    name = fields.Char(
        index="trigram",
        required=True,
        translate=True,
    )

    complete_name = fields.Char(
        compute="_compute_complete_name",
        recursive=True,
        store=True,
    )

    parent_id = fields.Many2one(
        "hr_hospital.disease",
        "Parent Disease",
        index=True,
        ondelete="cascade",
    )

    parent_path = fields.Char(
        index=True,
        unaccent=False,
    )

    child_id = fields.One2many(
        "hr_hospital.disease",
        "parent_id",
        "Child Disease",
    )

    # flake8
    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for dis in self:
            if dis.parent_id:
                dis.complete_name = "%s / %s" % (
                    dis.parent_id.complete_name,
                    dis.name,
                )
            else:
                dis.complete_name = dis.name

    @api.constrains("parent_id")
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_("You cannot create recursive disease."))

    @api.model
    def name_create(self, name):
        dis = self.create({"name": name})
        return dis.id, dis.display_name

    @api.depends_context("hierarchical_naming")
    def _compute_display_name(self):
        if self.env.context.get("hierarchical_naming", True):
            return super()._compute_display_name()
        for record in self:
            record.display_name = record.name
            return None
