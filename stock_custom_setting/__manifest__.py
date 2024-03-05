#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Custom Setting",
    "category": "Custom Setting",
    "description": "This is for enabling stock transport module",
    "summary": "Transport management system",
    "installable": True,
    "application": True,
    "auto_install": True,
    "license": "OEEL-1",
    "version": "1.0",
    "depends": ["base", "stock"],
    "data": [
        "views/res_config_settings_views.xml",
    ]
}