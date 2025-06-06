# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

{
    "name": "Point of Sale - Auto Parts",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point of Sale",
    "license": "OPL-1",
    "summary": "POS Auto Parts Point Of Sale Auto Parts POS Motorcycle Auto Parts POS Find Perfect Vehicle Auto Parts Choose Auto Parts Base On Vehicle Automobile spare Parts Retail POS Auto Parts POS System Asset Equipment Maintenance Vehicles Spare Parts Odoo",
    "description": """This module makes searching for auto parts it's as easy peasy. The POS search tool helps in choosing your auto parts base on vehicle make, vehicle model, type and model year very easily. Enter the vehicle details in the search field so it will display available auto parts. To shows general products, we provide a common products display option in POS.""",
    "version": "0.0.1",
    "depends": ["point_of_sale", 'sh_auto_part_vehicle'],
    "application": True,
    "data": [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'sh_pos_motorcycle/static/src/scss/pos.scss',
            'sh_pos_motorcycle/static/src/overrides/product_screen/*',
            'sh_pos_motorcycle/static/src/xml/ProductsWidgetControlPanel.xml',
            'sh_pos_motorcycle/static/src/apps/popups/*'
        ],
    },
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "price": 70,
    "currency": "EUR"
}
