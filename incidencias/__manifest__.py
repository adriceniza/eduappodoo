# -*- coding: utf-8 -*-
{
    'name': "incidencias",

    'summary': """
        Modulo de incidencias""",

    'description': """
        Registro de las incidencias en los municipios de Gran Canaria
    """,

    'author': "Adrián Ceniza",
    'website': "http://www.adriceniza.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : 'True'
}
