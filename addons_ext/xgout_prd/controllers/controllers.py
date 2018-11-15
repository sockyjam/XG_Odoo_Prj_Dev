# -*- coding: utf-8 -*-
from odoo import http

# class XgoutPrd(http.Controller):
#     @http.route('/xgout_prd/xgout_prd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgout_prd/xgout_prd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgout_prd.listing', {
#             'root': '/xgout_prd/xgout_prd',
#             'objects': http.request.env['xgout_prd.xgout_prd'].search([]),
#         })

#     @http.route('/xgout_prd/xgout_prd/objects/<model("xgout_prd.xgout_prd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgout_prd.object', {
#             'object': obj
#         })