# -*- coding: utf-8 -*-
{
    'name': 'Product CVE Linea',
    'summary': 'Adds a CVE-Linea catalog and field to products',
    'version': '18.0.1.1.0',
    'author': 'odoo-autoparts',
    'license': 'LGPL-3',
    'website': '',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
}