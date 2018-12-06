# -*- coding: utf-8 -*-
from odoo import http

# class Xgproduct(http.Controller):
#     @http.route('/xgproduct/xgproduct/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgproduct/xgproduct/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgproduct.listing', {
#             'root': '/xgproduct/xgproduct',
#             'objects': http.request.env['xgproduct.xgproduct'].search([]),
#         })

#     @http.route('/xgproduct/xgproduct/objects/<model("xgproduct.xgproduct"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgproduct.object', {
#             'object': obj
#         })