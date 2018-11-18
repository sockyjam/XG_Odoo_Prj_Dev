# -*- coding: utf-8 -*-

from odoo import models, fields


class Company(models.Model):
    _name = 'xgcrm.company'
    _description = 'XG CRM 体系的来往公司对象 '

    name = fields.Char(index=True, string='公司名称')

    person = fields.One2many('xgcrm.person', 'company', string='对方联系人')

    street = fields.Char(string='街道')
    city = fields.Char(string='城市')
    state_id = fields.Many2one("res.country.state", string='省份', ondelete='restrict')
    zip = fields.Char(change_default=True, string='邮编')
    email = fields.Char(string='电子邮件地址')
    phone = fields.Char(string='座机电话')
    mobile = fields.Char(string='移动电话')

    is_customer = fields.Boolean(string='是否客户?')
    is_supplier = fields.Boolean(string='是否供应商?')  # e.g. steel factory

    user_ids = fields.One2many('res.users', 'partner_id', string='我方负责人', auto_join=True,
                               context={'active_test': False})
    # contact_address = fields.Char(compute='_compute_contact_address', string='Complete Address')


class Person(models.Model):
    _name = 'xgcrm.person'
    _description = 'XG CRM 体系的来往联系人对象 '

    name = fields.Char(index=True, string='人员名字')

    company = fields.Many2one('xgcrm.company', string='对方所属公司')

    street = fields.Char(string='街道')
    city = fields.Char(string='城市')
    state_id = fields.Many2one("res.country.state", string='省份', ondelete='restrict')
    zip = fields.Char(change_default=True, string='邮编')
    email = fields.Char(string='电子邮件地址')
    phone = fields.Char(string='座机电话')
    mobile = fields.Char(string='移动电话')

    is_customer = fields.Boolean(string='是否客户?')
    is_supplier = fields.Boolean(string='是否供应商?')  # e.g. steel factory

    user_ids = fields.One2many('res.users', 'partner_id', string='我方负责人', auto_join=True,
                               context={'active_test': False})
