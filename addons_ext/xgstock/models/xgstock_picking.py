# -*- coding: utf-8 -*-

from odoo import models, fields, api

class xgstock_picking(models.Model):
    _name = 'xgstock.picking'
    _description = 'XG 入库'
    _rec_name = 'PRD_uuid'

    PRD_uuid = fields.Char(string='入库单号', required=True, index=True, copy=False)

    supplier = fields.Many2one('xgcrm.company', string='供应商')

    order_making_time = fields.Datetime(string='制单时间')
    expected_warehousing_time = fields.Date(string='预计入库时间')
    sums = fields.Float(string='总价')
    PRD_create_user = fields.Char(string='制单人')

    xgproduct_order_lines = fields.One2many('product.detailed', 'product_line', string='产品')

    xgstock_task_group = fields.Many2one('job.management',string='任务工作组')
    xgstock_position_id = fields.Many2one('xgstock.position',string='库位选择')
    state = fields.Selection([
        ('notStart', '发送调度员工单分配'),
        ('distribution', '调度员工单分配'),
        ('distributionEnd', '工单分配完成'),
        ('start', '入库审批通过'),
    ], string='状态', readonly=True, index=True, copy=False, default='notStart', track_visibility='onchange')

    @api.multi
    def button_not_start(self):
        self.write({'state': 'distribution'})

    @api.multi
    def button_start(self):
        self.write({'state': 'start'})

    @api.multi
    def button_distribution(self):
        self.write({'state': 'distributionEnd'})
        self.env['xgstock.xgin_prd'].write({'state': 'end'})
        self.env['product.detailed'].write({'state': 'true'})