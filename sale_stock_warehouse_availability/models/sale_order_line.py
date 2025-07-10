from odoo import fields, models, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    show_warehouse_availability = fields.Boolean(string="Show Warehouse Availability", default=True)
