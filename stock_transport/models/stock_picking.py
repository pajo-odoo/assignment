#-*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute="_compute_volume_weight")
    weight = fields.Float(string="Weight", compute="_compute_volume_weight")

    @api.depends("move_line_ids")
    def _compute_volume_weight(self):
        for record in self:
            temp_vol = 0
            temp_weight = 0

            for move_line in record.move_line_ids:
                temp_vol += (move_line.product_id.volume * move_line.quantity)
                temp_weight += (move_line.product_id.weight * move_line.quantity)

            record.volume = temp_vol
            record.weight = temp_weight
