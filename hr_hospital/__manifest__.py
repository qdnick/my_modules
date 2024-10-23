# Manifest modules hr_hospital
{
    "name": "HR Hospital hnn",
    "summary": "",
    "author": "qdnick",
    "category": "Customizations",
    "license": "LGPL-3",
    "version": "17.0.5.0.0",
    "depends": [
        "base",
        "mail",
    ],
    "external_dependencies": {
        "python": [],
    },
    "data": [
        "security/hr_hospital_group.xml",
        "security/hr_hospital_role.xml",
        "security/ir.model.access.csv",
        "wizard/disease_report_wizard_views.xml",
        "wizard/mass_update_doctor_wizard_views.xml",
        "views/specialty_views.xml",
        "views/doctor_views.xml",
        "views/patient_views.xml",
        "views/visit_views.xml",
        "views/disease_views.xml",
        "views/diagnosis_views.xml",
        "views/hospital_main_menu_views.xml",
        "reports/doctor_report.xml",
        "data/disease_data.xml",
    ],
    "demo": [
        "demo/specialty_demo.xml",
        "demo/doctor_demo.xml",
        "demo/patient_demo.xml",
        "demo/visit_demo.xml",
        "demo/diagnosis_demo.xml",
    ],
    "installable": True,
    "auto_install": False,
    "images": ["static/description/icon.png"],
}
