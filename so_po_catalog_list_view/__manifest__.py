# -*- coding: utf-8 -*-
{
    'name': "Catalog List View",
    'description': """
        list view for the product catalog
    """,
    'currency': 'USD',
    'price': '45.0',
    'license': 'LGPL-3',
    'author': "Bliss ERP Solution",
    'website': "https://www.blisserpsolution.com",
    'category': 'sale',
    'version': '18.0.1.0',
    'sequence': 1,
    'depends': ['base', 'sale', 'sale_management', 'product', 'purchase'],
    'data': [
        'views/product_tree_view.xml',
    ],
    'images': ['static/description/main_screenshot.png', 'static/description/icon.png'],
    'assets': {
        'web.assets_backend': [
            'so_po_catalog_list_view/static/src/js/**/*',
            'so_po_catalog_list_view/static/src/product_catalog/**/*.js',
            'so_po_catalog_list_view/static/src/product_catalog/**/*.xml',
        ],
    },
    'application': True,
    'installable': True,
    'support': 'contact@blisserpsolution.com',
}
