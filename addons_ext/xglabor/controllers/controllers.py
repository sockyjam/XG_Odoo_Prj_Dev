# -*- coding: utf-8 -*-
from odoo import http

# class Xglabor(http.Controller):
#     @http.route('/xglabor/xglabor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xglabor/xglabor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xglabor.listing', {
#             'root': '/xglabor/xglabor',
#             'objects': http.request.env['xglabor.xglabor'].search([]),
#         })

#     @http.route('/xglabor/xglabor/objects/<model("xglabor.xglabor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xglabor.object', {
#             'object': obj
#         })