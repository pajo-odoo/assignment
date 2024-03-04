#-*- coding: utf-8 -*-

from odoo import api, fields, models

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight (Kg)")
    max_volume = fields.Float(string="Max Volume")

    def _compute_display_name(self):
        for record in self:
            name = "{} ({:.2f}Kg, {:.2f})".format(record.name, record.max_weight, record.max_volume)
            record.display_name = name
