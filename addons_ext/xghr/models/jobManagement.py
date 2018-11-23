# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class jobManagement(models.Model):
    _name = 'job.management'
    _description = 'XG HR 工单管理 '
    _rec_name = 'uuid'

    uuid = fields.Char( string='工作单号', required=True, index=True, copy=False, default='New')  #需要方法生成
    work_describe = fields.Char(string='工作描述')
    work_type = fields.Char(string='工作种类')
    status = fields.Char(string='状态')
    prediction_time = fields.Date(string='预计工时')
    start_time = fields.Date(string='开始日期')
    Continued_time = fields.Date(string='持续时间')

    state = fields.Selection([
        ('notStart', '未开始'),
        ('start', '开始'),
        ('end', '完成'),
    ], string='状态', readonly=True, index=True, copy=False, default='notStart', track_visibility='onchange')

    job_management_line = fields.One2many('job.management.line', 'management_line_id',string='员工')



    @api.model
    def create(self, vals):
        '''
        form 表单提交默认 方法
        :param vals:
        :return:
        '''
        if vals.get('uuid', 'New') == 'New':
            vals['uuid'] = 'JM%s' % time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        return super(jobManagement, self).create(vals)


    @api.multi
    def button_start(self):
        '''
        button 按钮自定义方法
        :return:
        '''
        # print(self.uuid)
        # self.env['personnel.registration'].create({
        #     'name':'dailei1'
        # })
        self.write({'state': "end"})

    @api.multi
    def button_not_start(self):
        self.write({'state': 'start'})

    def _get_action(self, action_xmlid):
        # TDE TODO check to have one view + custo in methods
        action = self.env.ref(action_xmlid).read()[0]
        if self:
            action['display_name'] = self.display_name
        return action

    def button_action(self):
        return self._get_action('xghr.action_xghr_job_management_tree')

class  jobManagementLine(models.Model):
    _name = 'job.management.line'

    management_line_id = fields.Many2one('job.management', string='management_line_id')

    name = fields.Many2one('personnel.registration', string='名称', required=True)
        



