# -*- coding: utf-8 -*-

from odoo import models, fields


class Users(models.Model):
    _name = 'res.users'
    _inherit = ['res.users']


    is_customer = fields.Boolean('Is he a customer?')
    is_supplier = fields.Boolean('Is he a supplier')  # e.g. steel factory

