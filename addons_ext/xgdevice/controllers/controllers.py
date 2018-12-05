# -*- coding: utf-8 -*-
from odoo import http

# class Xgdevice(http.Controller):
#     @http.route('/xgdevice/xgdevice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgdevice/xgdevice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgdevice.listing', {
#             'root': '/xgdevice/xgdevice',
#             'objects': http.request.env['xgdevice.xgdevice'].search([]),
#         })

#     @http.route('/xgdevice/xgdevice/objects/<model("xgdevice.xgdevice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgdevice.object', {
#             'object': obj
#         })