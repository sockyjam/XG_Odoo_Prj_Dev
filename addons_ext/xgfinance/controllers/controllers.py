# -*- coding: utf-8 -*-
from odoo import http

# class Xgfinance(http.Controller):
#     @http.route('/xgfinance/xgfinance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgfinance/xgfinance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgfinance.listing', {
#             'root': '/xgfinance/xgfinance',
#             'objects': http.request.env['xgfinance.xgfinance'].search([]),
#         })

#     @http.route('/xgfinance/xgfinance/objects/<model("xgfinance.xgfinance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgfinance.object', {
#             'object': obj
#         })