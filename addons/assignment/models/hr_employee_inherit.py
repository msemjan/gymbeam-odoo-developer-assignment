from odoo import api, fields, models
import uuid
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    special_phone = fields.Char(string="Special Phone")
    salary = fields.Integer(string="Salary", required=True)
    tax = fields.Integer(string="Tax", required=True)
    total_salary = fields.Integer(
        string="Total Salary", compute="_compute_total_salary", store=True
    )

    i_love_gb = fields.Boolean(string="I Love GB")
    employee_contacts = fields.Binary(string="Employee Contacts")

    employee_number = fields.Char(
        string="Employee Number",
        required=True,
        tracking=True,
    )

    @api.depends("salary", "tax")
    def _compute_total_salary(self):
        for rec in self:
            rec.total_salary = rec.salary + rec.tax

    @api.model
    def create(self, vals):
        if not vals.get("special_phone"):
            vals["special_phone"] = "0901123456"
        return super().create(vals)

    def write(self, vals):
        if "special_phone" not in vals and not self.special_phone:
            vals["special_phone"] = "0901123456"

        if "employee_number" not in vals and not self.special_phone:
            vals["employee_number"] = str(uuid.uuid4())

        return super().write(vals)

    def open_send_email_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Send Emails",
            "view_mode": "form",
            "res_model": "wizard.send.email",
            "target": "new",
        }

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
