# -*- coding: utf-8 -*-
from odoo import http

# class XgstockReport(http.Controller):
#     @http.route('/xgstock_report/xgstock_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xgstock_report/xgstock_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xgstock_report.listing', {
#             'root': '/xgstock_report/xgstock_report',
#             'objects': http.request.env['xgstock_report.xgstock_report'].search([]),
#         })

#     @http.route('/xgstock_report/xgstock_report/objects/<model("xgstock_report.xgstock_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xgstock_report.object', {
#             'object': obj
#         })