# -*- coding: utf-8 -*-
{
    'name': "xglabor",

    'summary': """
        XG Labor management.
        """,

    'description': """
        管理量力劳务人员信息化，以及工作内容和分派。
    """,

    'author': "LLXG",
    'website': "http://www.scllxg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Employees',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'xgcrm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
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