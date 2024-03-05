#-*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import timedelta

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one(string="Dock", comodel_name="stock.transport.dock")
    vehicle = fields.Many2one(string="Vehicle", comodel_name="fleet.vehicle")
    vehicle_category_id = fields.Many2one(string="Category", comodel_name="fleet.vehicle.model.category")
    weight = fields.Float(string="Weight(kg)", compute="_compute_weight_volume", store=True)
    volume = fields.Float(string="Volume", compute="_compute_weight_volume", store=True)
    start_date = fields.Date(string="Start Date", compute="_compute_dates", store=True)
    end_date = fields.Date(string="End Date", compute="_compute_dates", store=True)
    moves_number = fields.Integer(string="Move Lines", compute="_compute_moves_number", store=True)
    transfers_number = fields.Integer(string="Transfer Lines", compute="_compute_transfers_number", store=True)

    @api.depends("vehicle_category_id", "vehicle_category_id.max_weight", "vehicle_category_id.max_volume")
    def _compute_weight_volume(self):
        self.weight = (sum(self.picking_ids.mapped("weight")) / self.vehicle_category_id.max_weight) * 100 if self.vehicle_category_id.max_weight != 0 else 0
        self.volume = (sum(self.picking_ids.mapped("volume")) / self.vehicle_category_id.max_volume) * 100 if self.vehicle_category_id.max_volume != 0 else 0

    @api.depends("create_date", "scheduled_date")
    def _compute_dates(self):
        for record in self:
            start_date = record.scheduled_date
            
            end_date = fields.Datetime.from_string(start_date) + timedelta(days=7)

            record.start_date = start_date
            record.end_date = end_date

    @api.depends("move_line_ids", "picking_ids")
    def _compute_moves_number(self):
        for record in self:
            record.moves_number = len(record.move_line_ids)
            record.transfers_number = len(record.picking_ids)
