#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Stock Transport",
    "category": "Stock Transport",
    "description": "This is for stock transporting",
    "summary": "Transport management system",
    "installable": True,
    "application": True,
    "license": "OEEL-1",
    "version": "1.0",
    "depends": ["base", "stock", "fleet", "stock_picking_batch"],
    "data": [
        "security/ir.model.access.csv",

        "views/stock_transport_docks_views.xml",
        "views/fleet_vehicle_model_views.xml",
        "views/stock_picking_batch_views.xml",
        "views/stock_transport_menus.xml",
    ]
}
