# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Labor(models.Model):
    _name = 'xglabor.labor'
    _description = 'XGLabor 劳务人员信息，包括姓名、身份证、工种等.'
    _rec_name = 'name'

    number = fields.Char(index=True, string='劳务编号', copy=False, readonly=True, default='New')
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
    labor_type = fields.Many2one('xglabor.type', string='工种类型')
    pay_type = fields.Selection([(1, u'计件型'), (2, u'固定工资型')], string='薪酬类型')
    grade = fields.Integer(string='能力等级')
    is_direct = fields.Boolean(string='是否定向工?')
    direct_company = fields.Many2one('xgcrm.company', string='定向公司')
    # work_order = fields.Many2one('xglabor.workorder', string='劳动工单')
    idcard_front = fields.Binary(string="身份证正面照")
    idcard_reverse = fields.Binary(string="身份证反面照")
    head_pic = fields.Binary(string="头像照片")

    @api.model
    def create(self, vals):
        if vals.get('number', 'New') == 'New':
            vals['number'] = self.env['ir.sequence'].next_by_code('xglabor.labor') or '/'
        return super(Labor, self).create(vals)


class LaborType(models.Model):
    _name = 'xglabor.type'
    _description = '劳务工种类型'

    name = fields.Char(index=True, string='工种名称')


class WorkOrder(models.Model):
    _name = 'xglabor.workorder'
    _description = '劳务工单，记录每次工作内容，每隔工单可能包含多个job'
    _rec_name = 'number'

    number = fields.Char(index=True, string='工单编号')
    # persons = fields.One2many('xglabor.labor', 'work_order', string='劳工人员列表')
    work_place = fields.Many2one('xgstock.position', string='工作场地')
    company = fields.Many2one('xgcrm.company', string='雇主公司')
    start_time = fields.Datetime(string='起始时间')
    end_time = fields.Datetime(string='结束时间')
    jobs = fields.One2many('xglabor.job', 'work_order', string='任务列表')
    confirm_person = fields.Many2one('res.users', string='审核人员')


class Job(models.Model):
    _name = 'xglabor.job'
    _description = '单次工作内容，job组成了工单;job为单人多次工作内容'

    person = fields.Many2one('xglabor.labor', string='劳工人员')
    type = fields.Many2one('xglabor.type', string='工作内容')
    pay_type = fields.Selection([(1, u'计件型'), (2, u'固定工资型')], string='薪酬类型')

    state = fields.Selection([('new', u'新建'), ('workover', u'工作完成'), ('confirm', u'确认'), ('pay', u'已付款')], string='状态')

    work_order = fields.Many2one('xglabor.workorder', string='关联工单')


