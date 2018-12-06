# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class product(models.Model):
    '''
    产品信息
    '''
    _name = 'xgproduct.product'
    _description = 'XG 产品信息'
    _rec_name = 'product_name'
    product_name = fields.Char(string='产品名称')
    sale_pirce = fields.Float(string='销售价格',digits=(6,2))
    purchase_pirce = fields.Float(string='进货价格', digits=(6, 2))
    product_type = fields.Many2one(string='产品类型',comodel_name='xgproduct.type')
    create_time = fields.Date(string='产品创建时间')
    create_user_id = fields.Integer()

    xgproduct_lines = fields.One2many('xgproduct.type', 'test_id')


    @api.model
    def create(self, vals):
        '''
        form 表单提交默认 方法
        :param vals:
        :return:
        '''
        print(self.env.user.name)
        vals['create_user_id'] = self.env.user.id
        vals['create_time'] =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return super(product, self).create(vals)

    @api.multi
    def write(self, vals):
        '''
        form 表单修改默认 方法
        :param vals:
        :return:
        '''
        vals['create_user_id'] = self.env.user.id
        vals['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return super(product, self).write(vals)
class productType(models.Model):
    '''
    产品类别
    '''
    _name = 'xgproduct.type'
    _description = '产品类别'
    _rec_name = 'product_type_name'

    product_type_id = fields.One2many(comodel_name='xgproduct.product',inverse_name='product_type')
    product_type_name = fields.Char(string='类别名称')

    test_id =fields.Many2one('xgproduct.product')

