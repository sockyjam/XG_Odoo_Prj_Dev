# -*- coding: utf-8 -*-
from odoo import http

# class Xgcontract(http.Controller):
#     @http.route('/xgcontract/xgcontract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgcontract/xgcontract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgcontract.listing', {
#             'root': '/xgcontract/xgcontract',
#             'objects': http.request.env['xgcontract.xgcontract'].search([]),
#         })

#     @http.route('/xgcontract/xgcontract/objects/<model("xgcontract.xgcontract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgcontract.object', {
#             'object': obj
#         })