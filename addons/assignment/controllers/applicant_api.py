import json

from odoo import http
from odoo.http import request


class ApplicantAPIController(http.Controller):
    @http.route(
        "/case_study/applicant/get",
        type="http",
        auth="public",
        methods=["POST"],
        csrf=False,
    )
    def create_applicants(self, **post):
        try:
            raw_data = request.httprequest.data
            if isinstance(raw_data, bytes):
                raw_data = raw_data.decode("utf-8")  # Decode bytes to str

            payload = json.loads(raw_data)
            candidates = payload.get("candidates", [])

            created = []

            for candidate in candidates:
                api_id = str(candidate["job"]["id"])  # fixed var name
                job = (
                    request.env["hr.job"]
                    .sudo()
                    .search([("api_id", "=", api_id)], limit=1)
                )

                if not job:
                    continue  # No matching job found, skip

                applicant_vals = {
                    "name": f"{candidate.get('firstname', '')} {candidate.get('surname', '')}",
                    "partner_name": candidate.get("title", ""),
                    "email_from": candidate.get("email", ""),
                    "partner_phone": candidate.get("phone", ""),
                    "gender": candidate.get("gender", ""),
                    "job_id": job.id,
                }

                applicant = request.env["hr.applicant"].sudo().create(applicant_vals)
                created.append(applicant.id)

            return request.make_response(
                json.dumps(
                    {
                        "status": "success",
                        "created_ids": created,
                    }
                ),
                headers=[("Content-Type", "application/json")],
                status=200,
            )

        except Exception as e:
            # Catch ALL errors
            return request.make_response(
                json.dumps(
                    {
                        "status": "error",
                        "error_message": str(e),
                    }
                ),
                headers=[("Content-Type", "application/json")],
                status=500,
            )
