# -*- coding: utf-8 -*-

from odoo import models, fields


class Company(models.Model):
    _name = 'xgcrm.company'
    _description = 'XG CRM 体系的来往公司对象 '

    name = fields.Char(index=True)

    person = fields.One2many('xgcrm.person', 'company', '联系人')

    street = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    zip = fields.Char(change_default=True)
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()

    is_customer = fields.Boolean('Is he a customer?')
    is_supplier = fields.Boolean('Is he a supplier')  # e.g. steel factory

    user_ids = fields.One2many('res.users', 'partner_id', string='销售负责人', auto_join=True,
                               context={'active_test': False})
    # contact_address = fields.Char(compute='_compute_contact_address', string='Complete Address')


class Person(models.Model):
    _name = 'xgcrm.person'
    _description = 'XG CRM 体系的来往联系人对象 '

    name = fields.Char(index=True)

    company = fields.Many2one('xgcrm.company', '所属公司')

    street = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    zip = fields.Char(change_default=True)
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()

    is_customer = fields.Boolean('Is he a customer?')
    is_supplier = fields.Boolean('Is he a supplier')  # e.g. steel factory

    user_ids = fields.One2many('res.users', 'partner_id', string='销售负责人', auto_join=True,
                               context={'active_test': False})
