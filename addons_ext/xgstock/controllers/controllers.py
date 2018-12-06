# -*- coding: utf-8 -*-
from odoo import http

class XgstockBase(http.Controller):
    @http.route('/xgstock_base/xgstock_base/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/test',  auth='public')
    def list(self):
        # return http.request.render('xgstock_base.listing', {
        #     'root': '/xgstock_base/xgstock_base',
        #     'objects': http.request.env['xgstock.xgin_prd'].search([]),
        # })
        data = http.request.env['xgstock.xgin_prd']
        a=data.read(fields=['PRD_uuid'])
        return '{"a":"ok"}'
    @http.route('/xgstock_ba.e/xgstock_base/objects/1', auth='public')
    def object(self, obj, **kw):
        return http.request.render('xgstock_base.object', {
            'object': obj
        })