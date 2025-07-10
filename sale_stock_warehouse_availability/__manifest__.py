# -*- coding: utf-8 -*-
#################################################################################
# Author      : CodersFort Info Solutions (<https://www.codersfort.com/>)
# Copyright(c): 2017-Present CodersFort Info Solutions.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.codersfort.com/>
#################################################################################

{
    "name": "Sales Product Warehouse Availability | Sales Warehouse Availability on Order Line  | Warehouse Availability on Sale Order Line | Sale Order Warehouse Availability",
    "summary": """
        This Odoo application is designed to enhance the efficiency of the sales team by providing real-time visibility into product availability across all warehouse. 
        Instead of checking stock levels for each warehouse individually, sales users can easily view consolidated inventory data within the sales interface.
    """,
    "sequence": "-100",
    "version": "18.1",
    "description": """
        This Odoo application is designed to enhance the efficiency of the sales team by providing real-time visibility into product availability across all warehouse. 
        Instead of checking stock levels for each warehouse individually, sales users can easily view consolidated inventory data within the sales interface.
    """,    
    "author": "CodersFort Info Solutions",
    "maintainer": "CodersFort Info Solutions",
    "license" :  "Other proprietary",
    "website": "https://www.codersfort.com",
    "images": ["images/sale_stock_warehouse_availability.png"],
    "category": "Sales",
    "depends": [
        "sale_stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
    ],
    "assets": {
       "web.assets_backend": [
            "sale_stock_warehouse_availability/static/src/js/*.*",
        ],
    },
    "installable": True,
    "application": True,
    "price"                 :  45,
    "currency"              :  "EUR",
}