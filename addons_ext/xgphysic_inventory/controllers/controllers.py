# -*- coding: utf-8 -*-
from odoo import http

# class XgphysicInventory(http.Controller):
#     @http.route('/xgphysic_inventory/xgphysic_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgphysic_inventory/xgphysic_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgphysic_inventory.listing', {
#             'root': '/xgphysic_inventory/xgphysic_inventory',
#             'objects': http.request.env['xgphysic_inventory.xgphysic_inventory'].search([]),
#         })

#     @http.route('/xgphysic_inventory/xgphysic_inventory/objects/<model("xgphysic_inventory.xgphysic_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgphysic_inventory.object', {
#             'object': obj
#         })