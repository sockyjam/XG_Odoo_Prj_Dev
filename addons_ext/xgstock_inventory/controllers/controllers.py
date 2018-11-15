# -*- coding: utf-8 -*-
from odoo import http

# class XgstockInventory(http.Controller):
#     @http.route('/xgstock_inventory/xgstock_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgstock_inventory/xgstock_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgstock_inventory.listing', {
#             'root': '/xgstock_inventory/xgstock_inventory',
#             'objects': http.request.env['xgstock_inventory.xgstock_inventory'].search([]),
#         })

#     @http.route('/xgstock_inventory/xgstock_inventory/objects/<model("xgstock_inventory.xgstock_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgstock_inventory.object', {
#             'object': obj
#         })