# -*- coding: utf-8 -*-

from odoo import models, fields, api

class labor(models.Model):
    _name = 'xglabor.labor'
    _description = 'XGLabor 劳务人员信息，包括姓名、身份证、工种等.'

    number = fields.Char(index=True, string='劳务编号')
    name = fields.Char(string='姓名')

    birthday = fields.Date(string='出生日期')
    native_place_province = fields.Many2one("res.country.state", string='省份', ondelete='restrict')
    native_place_city = fields.Char(string='城市')
    sex = fields.Selection([(1,u'男'),(2,u'女')], string=u'性别')
    telephone = fields.Char(string='手机号')
    idcard = fields.Char(string='身份证号')
    has_sick_history = fields.Boolean(string='有无病史')
    sick_history = fields.Text(string='病史说明')
    emergency_contact_person = fields.Char(string='紧急联络人')
    emergency_contact_telephone = fields.Char(string='紧急联络人电话')
    home_address = fields.Text(string='家庭住址')
    marital_status = fields.Boolean(string='婚姻状况')
    children_num = fields.Integer(string='子女数目')
    # labor_type = fields.Many2many()
    pay_type = fields.Selection([(1, u'计件型'), (2, u'固定工资型')], string='薪酬类型')
    grade = fields.Integer(string='能力等级')
    is_direct = fields.Boolean(string='是否定向工?')
    direct_company = fields.Many2one('xgcrm.company', string='定向公司')




class laborType(models.Model):
    _name = 'xglabor.type'
    _description = '劳务工种类型'

    name = fields.Char(index=True, string='工种名称')

