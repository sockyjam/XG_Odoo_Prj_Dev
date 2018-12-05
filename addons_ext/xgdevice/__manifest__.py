# -*- coding: utf-8 -*-
{
    'name': "xgdevice",

    'summary': """
        XGDevice, manage the devices of XG.""",

    'description': """
        管理设备，叉车、行车、吊秤、丝索，等跟劳务和安全有关的大型设备或安全设备.
        不管理小型无关设备，如号牌、指示牌、栏杆，等。
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
        # 'security/ir.model.access.csv',
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