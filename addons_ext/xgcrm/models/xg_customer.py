# -*- coding: utf-8 -*-

from odoo import models, fields


class XGCutstomer(models.Model):
    _name = 'xg.customer'
    _inherit = ['res.users']

    is_customer = fields.Boolean('Is he a customer?')
    is_supplier = fields.Boolean('Is he a supplier')  # e.g. steel factory

