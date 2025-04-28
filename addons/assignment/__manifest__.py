{
    "name": "I Love GymBeam",
    "version": "0.0.1",
    "depends": [
        "base",
        "hr_recruitment",
        "hr",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        "views/hr_applicant_views.xml",
        "views/hr_job_views.xml",
        "views/send_email_wizard_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/assignment/static/js/recruitment_form_validation.js",
            "/assignment/static/css/recruitment_form_validation.css",
        ],
    },
    "author": "Marek",
    "category": "Uncategorized",
    "summary": "I love GymBeam Addon",
    "description": "Module case study.",
    "installable": True,
    "application": False,
    "license": "GPL-3",
}
