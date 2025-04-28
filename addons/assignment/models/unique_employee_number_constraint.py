from odoo import models, api
from odoo.exceptions import ValidationError


class UniqueEmployeeNumberConstraint(models.AbstractModel):
    _name = "employee.number.constraint"
    _description = "Constraint to ensure unique employee number"

    @api.constrains("employee_number")
    def _check_unique_employee_number(self):
        for record in self:
            employee_conflict = self.env["hr.employee"].search(
                [
                    ("employee_number", "=", record.employee_number),
                    ("id", "!=", record.id),
                ],
                limit=1,
            )

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
