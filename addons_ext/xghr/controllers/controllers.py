# -*- coding: utf-8 -*-
from odoo import http

# class Xghr(http.Controller):
#     @http.route('/xghr/xghr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xghr/xghr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xghr.listing', {
#             'root': '/xghr/xghr',
#             'objects': http.request.env['xghr.xghr'].search([]),
#         })

#     @http.route('/xghr/xghr/objects/<model("xghr.xghr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xghr.object', {
#             'object': obj
#         })