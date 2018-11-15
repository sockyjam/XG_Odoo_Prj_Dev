# -*- coding: utf-8 -*-
from odoo import http

# class XginPrd(http.Controller):
#     @http.route('/xgin_prd/xgin_prd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgin_prd/xgin_prd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgin_prd.listing', {
#             'root': '/xgin_prd/xgin_prd',
#             'objects': http.request.env['xgin_prd.xgin_prd'].search([]),
#         })

#     @http.route('/xgin_prd/xgin_prd/objects/<model("xgin_prd.xgin_prd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgin_prd.object', {
#             'object': obj
#         })