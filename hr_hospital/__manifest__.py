{
    'name': 'HR Hospital',
    'summary': '',
    'author': 'qdnick',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.0.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [

        'security/ir.model.access.csv',
        'views/hospital_main_menu_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/visit_views.xml',
        'views/disease_views.xml',
        'data/disease_data.xml'
    ],

    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],

}
