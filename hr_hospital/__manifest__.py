# Manifest modules hr_hospital
{
    'name': 'HR Hospital',
    'summary': '',
    'author': 'qdnick',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.2.0.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/ir.model.access.csv',
        'wizard/disease_report_wizard_views.xml',
        'wizard/mass_update_doctor_wizard_views.xml',
        'views/specialty_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/visit_views.xml',
        'views/disease_views.xml',
        'views/diagnosis_views.xml',
        'views/hospital_main_menu_views.xml',
    ],

    'demo': [
        'demo/disease_demo.xml',
        'demo/specialty_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],


}
