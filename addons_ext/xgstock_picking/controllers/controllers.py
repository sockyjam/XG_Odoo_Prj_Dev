# -*- coding: utf-8 -*-
from odoo import http

# class XgstockPicking(http.Controller):
#     @http.route('/xgstock_picking/xgstock_picking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgstock_picking/xgstock_picking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgstock_picking.listing', {
#             'root': '/xgstock_picking/xgstock_picking',
#             'objects': http.request.env['xgstock_picking.xgstock_picking'].search([]),
#         })

#     @http.route('/xgstock_picking/xgstock_picking/objects/<model("xgstock_picking.xgstock_picking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgstock_picking.object', {
#             'object': obj
#         })