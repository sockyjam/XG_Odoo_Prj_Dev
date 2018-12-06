# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
class xgin_prd(models.Model):
    _name = 'xgstock.xgin_prd'
    _description = 'XG 入库预报'
    _rec_name = 'PRD_uuid'

    PRD_uuid = fields.Char(string='入库单号', required=True, index=True, copy=False, default='New')

    supplier = fields.Many2one('xgcrm.company', string='供应商', domain=[('is_supplier', '=', True)])

    order_making_time = fields.Datetime(string='制单时间')
    expected_warehousing_time = fields.Date(string='预计入库时间')
    sums = fields.Float(compute='_compute_sums', string='总价')
    PRD_create_user = fields.Char(string='制单人')

    xgproduct_order_lines = fields.One2many('xgstock.xgin.prd.order.line', 'xgin_prd_line', string='产品')

    state = fields.Selection([
        ('pending', '预报待审批'),
        ('adopt', '审批通过 确认入库'),
        ('warehousing', '已确认入库'),
        ('end', '入库已完成'),
    ], string='状态', readonly=True, index=True, copy=False, default='pending', track_visibility='onchange')

    @api.multi
    def button_pending(self):
        '''
        1。修改当前状态，
        2。创建入库单
        3。产品数据 移至 库存
        :return:
        '''
        self.write({'state': 'adopt'})


    @api.multi
    def button_adopt(self):
        '''
        1。修改当前状态，
        2。创建入库单
        3。产品数据 移至 库存
        :return:
        '''
        self.write({'state': 'warehousing'})
        self.env['xgstock.picking'].create(
            {'PRD_uuid': self.PRD_uuid,
             'supplier': self.supplier.id,
             'order_making_time': self.order_making_time,
             'expected_warehousing_time': self.expected_warehousing_time,
             'sums': self.sums,
             'PRD_create_user': self.PRD_create_user,
             }
        )

        res = self.env['xgstock.picking'].search([('PRD_uuid', '=', self.PRD_uuid)])

        for i in self.xgproduct_order_lines:
            self.env['product.detailed'].create(
                {'product_name': i.xgproduct_line.product_name,
                 'product_num': i.product_num,
                 'product_line':res.id
                 }
            )

    @api.multi
    @api.depends('xgproduct_order_lines')
    def _compute_sums(self):
        sum_pirce = 0
        for order in self.xgproduct_order_lines:
            sum_pirce += order.product_pirce
        self.sums = sum_pirce

    @api.model
    def create(self, vals):
        '''
        form 表单提交默认 方法
        :param vals:
        :return:
        '''
        vals['PRD_create_user'] = self.env.user.name
        vals['PRD_uuid'] = 'RK%s' % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        vals['order_making_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(vals)
        return super(xgin_prd, self).create(vals)


class xgin_prd_order_line(models.Model):
    _name = 'xgstock.xgin.prd.order.line'
    _description = '关联模块'
    _rec_name = 'xgproduct_line'

    xgproduct_line= fields.Many2one('xgproduct.product', string='产品名称', change_default=True, required=True)

    xgin_prd_line = fields.Many2one('xgstock.xgin_prd')

    xgin_apply_line = fields.Many2one('xgstock.xgin_apply')
    purchase_pirce = fields.Float(string='采购价格')
    product_num = fields.Integer(string='产品数量')
    product_pirce =fields.Float(string='小计', compute='_compute_product_pirce', store=True)


    @api.multi
    @api.depends('product_num', 'purchase_pirce')
    def _compute_product_pirce(self):
        for i in self:
            i.product_pirce = i.purchase_pirce * i.product_num


    @api.onchange('xgproduct_line')
    def purchase_pirce_onchange(self):
        result = {}
        print(self.xgproduct_line)
        if not self.xgproduct_line:
            return result
        self.purchase_pirce = self.xgproduct_line.purchase_pirce
