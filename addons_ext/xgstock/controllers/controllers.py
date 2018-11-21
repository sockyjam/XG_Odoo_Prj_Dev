# -*- coding: utf-8 -*-
from odoo import http

# class XgstockBase(http.Controller):
#     @http.route('/xgstock_base/xgstock_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgstock_base/xgstock_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgstock_base.listing', {
#             'root': '/xgstock_base/xgstock_base',
#             'objects': http.request.env['xgstock_base.xgstock_base'].search([]),
#         })

#     @http.route('/xgstock_base/xgstock_base/objects/<model("xgstock_base.xgstock_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgstock_base.object', {
#             'object': obj
#         })