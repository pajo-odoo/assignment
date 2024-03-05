#-*- coding: utf-8 -*-

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock_transport = fields.Boolean(string="Stock Transport")