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
    'depends': ['base', 'xgproduct', 'xgcrm', 'xghr'],

    # always loaded
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/templates.xml',
        'views/xgin_prd_view.xml',
        'views/xgout_prd_view.xml',
        'views/xgin_apply_view.xml',
        'views/xgout_apply_view.xml',
        'views/product_detailed_view.xml',
        'views/xgstock_picking_view.xml',
        'views/xgstock_odo_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
