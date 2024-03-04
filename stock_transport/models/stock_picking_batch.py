#-*- coding: utf-8 -*-

from odoo import api, fields, models

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one(string="Dock", comodel_name="stock.transport.dock")
    vehicle = fields.Many2one(string="Vehicle", comodel_name="fleet.vehicle")
    vehicle_category_id = fields.Many2one(string="Category", comodel_name="fleet.vehicle.model.category")
    weight = fields.Float(string="Weight(kg)", compute="_compute_weight_volume")
    volume = fields.Float(string="Volume", compute="_compute_weight_volume")

    @api.depends("vehicle_category_id")
    def _compute_weight_volume(self):
        self.ensure_one()

        move_line_ids = []

        weight = 0
        volume = 0

        for move_line_id in self.move_line_ids:
            move_line_ids.append(move_line_id.id)

        move_lines = self.env["stock.move.line"].browse(move_line_ids)

        for move_line in move_lines:
            weight += move_line.product_id.weight * move_line.quantity
            volume += move_line.product_id.volume * move_line.quantity
        
        
        self.weight = weight / self.vehicle_category_id.max_weight if self.vehicle_category_id.max_weight != 0 else 0
        self.volume = volume / self.vehicle_category_id.max_volume if self.vehicle_category_id.max_volume != 0 else 0
