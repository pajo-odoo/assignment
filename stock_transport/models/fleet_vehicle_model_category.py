#-*- coding: utf-8 -*-

from odoo import api, fields, models

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight (Kg)")
    max_volume = fields.Float(string="Max Volume")

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight}Kg,{record.max_volume}m\u00b3)"
