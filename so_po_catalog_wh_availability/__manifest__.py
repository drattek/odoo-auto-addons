# -*- coding: utf-8 -*-
{
    'name': "Catalog Warehouse Availability",
    'summary': "Extend catalog list view with per-warehouse availability columns",
    'description': """
        Extends the product catalog list view (so_po_catalog_list_view) to show
        warehouse availability per item, by adding a column for each warehouse.
        Columns are injected server-side in the list view, without JavaScript.
    """,
    'version': '18.0.1.1',
    'license': 'LGPL-3',
    'author': "Custom",
    'website': "",
    'category': 'Sales',
    'depends': ['web', 'sale', 'sale_management', 'product', 'stock', 'sale_stock', 'so_po_catalog_list_view'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
