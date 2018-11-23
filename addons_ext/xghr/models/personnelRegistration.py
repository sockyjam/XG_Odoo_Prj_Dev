# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.base.models import res_users
class personnelRegistration(models.Model):
    _name = 'personnel.registration'
    _description = 'XG HR 人员登记'

    personnel_id = fields.Many2one('personnel.group', string='所属工种')
    management_lines = fields.One2many('job.management.line', 'name')
    name = fields.Char(string='员工名称')
    # login=fields.Many2one('res.users', string='login', index=True, track_visibility='onchange',
    #                 default=lambda self: self.env.user)
    # pwd=fields.Many2one('res.users', string='pwd', index=True, track_visibility='onchange',
    #                 default=lambda self: self.env.password)
    company_id = fields.Many2one('res.company', '公司')
    street = fields.Char(string='街道')
    city = fields.Char(string='城市')
    state_id = fields.Many2one("res.country.state", string='省份', ondelete='restrict')
    zip = fields.Char(change_default=True, string='邮编')
    email = fields.Char(string='电子邮件地址')
    phone = fields.Char(string='座机电话')
    mobile = fields.Char(string='移动电话')
    image = fields.Binary(string="上传合同照片")


    @api.multi
    def print_quotation(self,vals):
        print(vals['name'])
        self.env['res.users'].create(
            [{
                 'active': True,
                 'company_ids': [[6, False, [1]]],
                 'company_id': 1,
                 'lang': 'en_US',
                 'tz': 'Europe/Brussels',
                 'notification_type': 'email',
                 'odoobot_state': 'not_initialized',
                 'image': False,
                 '__last_update': False,
                 'name': vals['name'],
                 'email': False,
                 'login': vals['name'],
                 'password': '123',
                 'action_id': False,
                 'alias_id': False,
                 'alias_contact': False,
                 'signature': '<p><br></p>',
                 'groups_id': [(6, 0, [1, 35, 23, 29, 42, 36, 27, 7, 6, 20, 19, 34, 28, 43])]
                 }]
        )


    @api.model
    def create(self, vals):
        # self.print_quotation(vals)
        return super(personnelRegistration, self).create(vals)



class personnelGroup(models.Model):
    _name = 'personnel.group'
    _description = '人员 分组'
    _rec_name = 'group_name'
    personnel_ids = fields.One2many('personnel.registration', 'personnel_id')
    group_name = fields.Char(string='工种名称')
