# -*- coding: utf-8 -*-
{
    'name': "eduapp",

    'summary': """
        Modulo de eduapp
        """,
    'description': """
        Long description of module's purpose
    """,

    'author': "Adrián Ceniza",
    'website': "http://www.eduapp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/sessions_report_view.xml',
        'reports/sessions_report.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : 'True',
}
