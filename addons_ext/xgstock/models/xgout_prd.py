# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
class xgout_prd(models.Model):
    _name = 'xgstock.xgout_prd'
    _description = 'XG 出库预报'
    _rec_name = 'PRD_uuid'

    PRD_uuid = fields.Char(string='入库单号', required=True, index=True, copy=False, default='New')

    supplier = fields.Many2one('xgcrm.company', string='客户', domain=[('is_customer', '=', True)])

    order_making_time = fields.Datetime(string='制单时间')
    expected_warehousing_time = fields.Date(string='预计出库时间')
    PRD_create_user = fields.Char(string='制单人')

    xgproduct_order_lines = fields.One2many('xgstock.xgout.prd.order.line', 'xgout_prd_line', string='产品')

    state = fields.Selection([
        ('pending', '预报待审批'),
        ('adopt', '审批通过 确认出库'),
        ('warehousing', '已确认出库'),
        ('senddby', '发送调度员工单分配'),
        ('distribution', '调度员工单分配'),
        ('distributionEnd', '工单分配完成'),
        ('success', '出库审批通过'),
        ('end', '出库已完成'),
    ], string='状态', readonly=True, index=True, copy=False, default='pending', track_visibility='onchange')

    xgstock_task_group = fields.Many2one('job.management', string='任务工作组')
    xgstock_position_id = fields.Many2one('xgstock.position', string='库位选择')
    @api.multi
    def button_pending(self):
        '''
        :return:
        '''
        self.write({'state': 'adopt'})
        self.env['xgstock.odo'].create(
            {'PRD_uuid': self.PRD_uuid,
             'supplier': self.supplier.id,
             'order_making_time': self.order_making_time,
             'expected_warehousing_time': self.expected_warehousing_time,
             'PRD_create_user': self.PRD_create_user,
             }
        )

    @api.multi
    def button_senddby(self):
        '''
        1。修改当前状态，
        :return:
        '''
        self.write({'state': 'distribution'})


    @api.multi
    def button_adopt(self):
        '''
        1。修改当前状态，
        :return:
        '''
        self.write({'state': 'warehousing'})
    @api.multi
    def button_distribution(self):
        '''
        1。修改当前状态，
        :return:
        '''
        self.write({'state': 'distributionEnd'})

    @api.multi
    def button_success(self):
        '''
        1。修改当前状态，
        :return:
        '''
        self.write({'state': 'end'})
        # for i in self.xgproduct_order_lines:
        #     self.env['product.detailed'].write(
        #         {
        #             'product_name': i.xgproduct_line.product_name,
        #          }
        #     )

    @api.model
    def create(self, vals):
        '''
        form 表单提交默认 方法
        :param vals:
        :return:
        '''
        vals['PRD_create_user'] = self.env.user.name
        vals['PRD_uuid'] = 'CK%s' % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        vals['order_making_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return super(xgout_prd, self).create(vals)


class xgout_prd_order_line(models.Model):
    _name = 'xgstock.xgout.prd.order.line'
    _description = '关联模块'
    _rec_name = 'product_detailed_id'

    product_detailed_id = fields.Many2one('product.detailed', string='产品名称', change_default=True, required=True)

    xgout_prd_line = fields.Many2one('xgstock.xgout_prd')

    product_detailed_num = fields.Integer(string='产品数量')



    # @api.onchange('product_detailed_id')
    # def purchase_pirce_onchange(self):
    #     result = {}
    #     if not self.product_detailed_id:
    #         return result
    #     self.purchase_pirce = self.product_detailed_id.purchase_pirce
