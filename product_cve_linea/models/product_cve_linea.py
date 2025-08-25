# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductCveLinea(models.Model):
    _name = 'product.cve.linea'
    _description = 'CVE Linea'
    _order = 'name'

    name = fields.Char(required=True, translate=False)
    code = fields.Char(string='Code', help='Optional unique code for the CVE Linea entry')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique.'),
    ]
