# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_cve_linea_id = fields.Many2one(
        comodel_name='product.cve.linea',
        string='CVE-Linea',
        help='Catalog value indicating the CVE Linea for this product.'
    )

    x_cross = fields.Text(
        string='XCross',
        help='Free-form compatibility notes between auto parts. Large text; not a catalog.'
    )
