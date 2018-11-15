# -*- coding: utf-8 -*-
from odoo import http

# class Xgstorage(http.Controller):
#     @http.route('/xgstorage/xgstorage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgstorage/xgstorage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgstorage.listing', {
#             'root': '/xgstorage/xgstorage',
#             'objects': http.request.env['xgstorage.xgstorage'].search([]),
#         })

#     @http.route('/xgstorage/xgstorage/objects/<model("xgstorage.xgstorage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgstorage.object', {
#             'object': obj
#         })