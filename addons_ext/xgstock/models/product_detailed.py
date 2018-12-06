# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_detailed(models.Model):
    _name = 'product.detailed'
    _description = '库存模块'
    _rec_name = 'product_name'

    product_name = fields.Char(string='产品名称')
    product_num = fields.Integer(string='产品数量')
    state = fields.Selection([
        ('false', '假'),
        ('true', '真'),
    ], string='状态', readonly=True, index=True, copy=False, default='false', track_visibility='onchange')
    product_line = fields.Many2one('xgstock.picking')
    xgout_prd_line = fields.One2many('xgstock.xgout.prd.order.line', 'product_detailed_id')