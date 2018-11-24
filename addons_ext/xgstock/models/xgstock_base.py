# -*- coding: utf-8 -*-

from odoo import models, fields
'''
XGStock_Base is basic element for entire XGStock.
You can define basic information here, the element here can be used by other models in this module.
And can be inherited by other modules.
'''

class WareHouse(models.Model):
    _name = 'xgstock.warehouse'
    _description = 'XGStock 仓库，仓库是独立的一个仓储空间。区分一个仓库的界限是，整个仓库属于一个管理方，或在一个整体的空间。'

    name = fields.Char(index=True, string='仓库名称')
    owner_company = fields.Many2one('res.company', string='属于公司')
    charge_person = fields.One2many('res.users', 'partner_id', string='负责人员', auto_join=True,
                               context={'active_test': False})

    street = fields.Char(string='街道')
    city = fields.Char(string='城市')
    state_id = fields.Many2one("res.country.state", string='省份', ondelete='restrict')
    zip = fields.Char(change_default=True, string='邮编')
    email = fields.Char(string='电子邮件地址')
    phone = fields.Char(string='座机电话')
    mobile = fields.Char(string='移动电话')

    position = fields.One2many('xgstock.position', 'warehouse', string='库位')



class Position(models.Model):
    _name = 'xgstock.position'
    _description = 'XGStock 库位，库位是从属于仓库Warehouse的，仓库由许多库位组成，每个库位可以单独指定负责人员，也可能被出租给商户。'

    name = fields.Char(index=True, string='库位名称或编号')
    warehouse = fields.Many2one('xgstock.warehouse', string='从属仓库')
    comment = fields.Char(string='其他描述')
    size = fields.Integer(string='库位面积(m2)')
    type = fields.Selection([
        ('self', "公司自有"),
        ('rent', "出租客户"),
        ('share', "灵活共有"),
        ('other', "其他"),
    ], string='库位性质')
    rent_company = fields.Many2one('xgcrm.company', string='出租从属客户公司')


class Product(models.Model):
    _name = 'xgstock.product'
    _description = 'XGStock 产品，产品是工厂生产出来的类型化产品。'

    name = fields.Char(index=True, string='产品名称')
    spec_material = fields.Char(string='材质规格')
    spec_size = fields.Char(string='尺寸规格')
    factory = fields.Many2one('xgcrm.company', string='钢厂/供应商')




