# -*- coding: utf-8 -*-
{
    'name': "XGCRM",

    'summary': """
        CRM module for Liangli XinGang Inc.""",

    'description': """
        It is used for managing client and supplier.
    """,

    'author': "LLXG",
    'website': "http://www.scllxg.com/",


    'category': 'User types',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/group_rule.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/xgcrm_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}