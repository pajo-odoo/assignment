#-*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute="_compute_volume")
    weight = fields.Float(string="Weight", compute="_compute_volume")

    @api.depends("move_line_ids")
    def _compute_volume(self):

        temp_vol = 0
        temp_weight = 0

        for move_line in self.move_line_ids:
            temp_vol += (move_line.product_id.volume * move_line.quantity)
            temp_weight += (move_line.product_id.weight * move_line.quantity)

        self.volume = temp_vol
        self.weight = temp_weight
