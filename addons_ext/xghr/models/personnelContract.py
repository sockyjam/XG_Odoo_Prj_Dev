# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _

class xghr(models.Model):
    _name = 'personnel.contract'

    name = fields.Char("test")
    value = fields.Char("test2")
    image_medium = fields.Binary(
        "图片", compute='_compute_images', inverse='_set_image_medium',
        help="Image of the product variant (Medium-sized image of product template if false).")

    @api.one
    def _set_image_medium(self):
        self._set_image_value(self.image_medium)
    @api.one
    def _compute_images(self):
        if self._context.get('bin_size'):
            self.image_medium = self.image_variant
        else:
            resized_images = tools.image_get_resized_images(self.image_variant, return_big=True, avoid_resize_medium=True)
            self.image_medium = resized_images['image_medium']
        if not self.image_medium:
            self.image_medium = self.product_tmpl_id.image_medium
