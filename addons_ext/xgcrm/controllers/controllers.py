# -*- coding: utf-8 -*-
from odoo import http

# class Xgcrm(http.Controller):
#     @http.route('/xgcrm/xgcrm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgcrm/xgcrm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgcrm.listing', {
#             'root': '/xgcrm/xgcrm',
#             'objects': http.request.env['xgcrm.xgcrm'].search([]),
#         })

#     @http.route('/xgcrm/xgcrm/objects/<model("xgcrm.xgcrm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgcrm.object', {
#             'object': obj
#         })