# -*- coding: utf-8 -*-
{
    'name': "xgstock_base",

    'summary': """
        Base information and element for XGStock function.
        Such like product, warehouse, place, productclass, and so on.""",

    'description': """
        Maintain basic elements. This should be depended by xgin_prd, xgout_prd, xgstock_xxx... 
    """,

    'author': "Liangli Xingang",
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
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}