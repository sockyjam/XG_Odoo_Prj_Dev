# -*- coding: utf-8 -*-
{
    'name': "XGStock",

    'summary': """
        XGStock function.
        Such like product, warehouse, place, productclass, and so on.""",

    'description': """
        XG Stock module 
    """,

    'author': "LLXG",
    'website': "http://www.scllxg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}