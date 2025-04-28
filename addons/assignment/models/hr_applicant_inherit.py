from odoo import models, fields, api
import uuid
from odoo.exceptions import ValidationError


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    employee_number = fields.Char(
        string="Employee Number",
        tracking=True,
        required=True,
    )

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        string="Gender",
        tracking=True,
        default='other',
    )

    @api.model
    def create(self, vals):
        if "employee_number" not in vals:
            vals["employee_number"] = str(uuid.uuid4())

        return super().create(vals)

    @api.constrains("employee_number")
    def _check_unique_employee_number(self):
        for record in self:
            if not record.employee_number:
                continue

            # Check in hr.employee
            employee_conflict = self.env["hr.employee"].search(
                [
                    ("employee_number", "=", record.employee_number),
                    ("id", "!=", record.id),
                ],
                limit=1,
            )

            # Check in hr.applicant
            applicant_conflict = self.env["hr.applicant"].search(
                [
                    ("employee_number", "=", record.employee_number),
                    ("id", "!=", record.id),
                ],
                limit=1,
            )

            if employee_conflict or applicant_conflict:
                raise ValidationError(
                    f"The employee number '{record.employee_number}' must be unique!"
                )
