# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Xgcontract(models.Model):
    _name = 'xgcontract.xgcontract'
    _description = '合同管理'

    name = fields.Char(string="合同名称", required=True)
    start = fields.Datetime(string="开始日期", required=True)
    end = fields.Datetime(string="到期日期", required=True)
    type = fields.Boolean(string="合同类型", required=True)
    file = fields.Binary(string="上传附件")
    is_expired = fields.Boolean(string="已过期", compute='_compute_is_expired')

    state = fields.Selection([
        ('one', '搁置'),
        ('two', '已签'),
        ('three', '未签'),
        ('four', '到期'),
    ], default='three', string='合同状态')

    category_id_p = fields.Many2one('company.company', string='隶属公司', required=True, readonly=True)  # 采购

    category_id_m = fields.Many2one('company.company', string='隶属公司')  # 销售

    company_ids_p = fields.One2many('company.company', 'category_id_p')

    company_ids_m = fields.One2many('company.company', 'category_id_m')

    description = fields.Text()

    @api.depends('state')
    @api.multi
    def _compute_is_expired(self):
        for record in self:
            print('#############################', type(record.state))
            if record.state == 'four':
                record.is_expired = True
            else:
                record.is_expired = False


class Company(models.Model):
    _name = 'company.company'
    _description = '企业管理'

    name = fields.Char(string="公司名称", required=True)
    person = fields.Char(string="法人代表", required=True)

    company_ids_p = fields.One2many('xgcontract.xgcontract', 'category_id_p', string='采购合同')

    company_ids_m = fields.One2many('xgcontract.xgcontract', 'category_id_m', string='销售合同')

    category_id_p = fields.Many2one('xgcontract.xgcontract', string='采购合同')

    category_id_m = fields.Many2one('xgcontract.xgcontract', string='销售合同')

    description = fields.Text()
