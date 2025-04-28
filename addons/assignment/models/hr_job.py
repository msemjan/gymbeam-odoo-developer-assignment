from odoo import models, fields, api
import uuid


class HrJob(models.Model):
    _inherit = "hr.job"

    api_id = fields.Char(string="API ID", required=True)

    @api.model
    def create(self, vals):
        if not vals.get("api_id"):
            vals["api_id"] = str(uuid.uuid4())

        return super().create(vals)
