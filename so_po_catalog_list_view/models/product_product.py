from odoo import models, fields, api
from odoo.tools.misc import unique


class ProductProduct(models.Model):
    _inherit = 'product.product'

    order_id = fields.Many2one('sale.order', string='Sale Order', compute='_compute_order_id', store=False)
    product_so_qty = fields.Integer('QTY', compute='_compute_product_so_qty', inverse='_inverse_product_so_qty',
                                    store=False)
    order_po_id = fields.Many2one('purchase.order', string='Purchase Order', compute='_compute_order_id')

    @api.depends('order_id', 'order_po_id')
    def _compute_product_so_qty(self):
        for product in self:
            res_model = dict(product.env.context or {}).get('product_catalog_order_model')
            if res_model == 'sale.order':
                order_lines = product.order_id.order_line.filtered(lambda line: line.product_id.id == product.id)
                if order_lines:
                    product.product_so_qty = sum(line.product_uom_qty for line in order_lines)
                else:
                    product.product_so_qty = 0
            if res_model == 'purchase.order':
                order_lines = self.order_po_id.order_line.filtered(lambda line: line.product_id.id == product.id)
                if order_lines:
                    product.product_so_qty = sum(line.product_qty for line in order_lines)
                else:
                    product.product_so_qty = 0
    def _inverse_product_so_qty(self):
        for product in self:
            res_model = dict(product.env.context or {}).get('product_catalog_order_model')
            if res_model == 'sale.order':
                order_line = product.order_id.order_line.filtered(lambda line: line.product_id.id == product.id)
                if order_line:
                    order_line.product_uom_qty = product.product_so_qty
            if res_model == 'purchase.order':
                order_line = product.order_po_id.order_line.filtered(lambda line: line.product_id.id == product.id)
                if order_line:
                    order_line.product_qty = product.product_so_qty

    @api.depends()
    def _compute_order_id(self):
        for product in self:
            order_id = dict(product.env.context or {}).get('order_id')
            product.order_id = self.env['sale.order'].browse(order_id)
            product.order_po_id = self.env['purchase.order'].browse(order_id)

    is_in_order = fields.Boolean(
        string='In Sale Order',
        compute='_compute_is_in_order',
        default=True
    )

    @api.depends('order_id')
    def _compute_is_in_order(self):
        for product in self:
            res_model = dict(product.env.context or {}).get('product_catalog_order_model')
            if res_model == 'sale.order':
                product.is_in_order = any(line.product_id == product for line in product.order_id.order_line)
            if res_model == 'purchase.order':
                product.is_in_order = any(line.product_id == product for line in product.order_po_id.order_line)

    def action_add_products_to_order(self):
        if not self.order_id:
            return
        product_ids = self.env.context.get('active_ids', [])
        res_model = dict(self.env.context or {}).get('product_catalog_order_model')
        for product_id in product_ids:
            product = self.env['product.product'].browse(product_id)
            if res_model == 'sale.order':
                self.order_id.order_line.create({
                    'order_id': self.order_id.id,
                    'product_id': product.id,
                    'name': product.name,
                    'product_uom_qty': 1,
                    'price_unit': product.lst_price,
                })
                product.is_in_order = True
            if res_model == 'purchase.order':
                self.order_po_id.order_line.create({
                    'order_id': self.order_id.id,
                    'product_id': product.id,
                    'name': product.name,
                    'product_qty': 1,
                    'price_unit': product.lst_price,
                })
                product.is_in_order = True
        return True

    def action_add_product_to_order(self):
        if not self.order_id:
            return
        res_model = dict(self.env.context or {}).get('product_catalog_order_model')
        product = self.env['product.product'].browse(self.id)
        if res_model == 'sale.order':
            self.order_id.order_line.create({
                'order_id': self.order_id.id,
                'product_id': product.id,
                'name': product.name,
                'product_uom_qty': 1,
                'price_unit': product.lst_price,
            })
            self.is_in_order = True
        if res_model == 'purchase.order':
            self.order_po_id.order_line.create({
                'order_id': self.order_id.id,
                'product_id': product.id,
                'name': product.name,
                'product_qty': 1,
                'price_unit': product.lst_price,
            })
        return True

    def action_remove_product_from_order(self):
        res_model = dict(self.env.context or {}).get('product_catalog_order_model')
        if res_model == 'sale.order':
            order_line = self.order_id.order_line.filtered(lambda line: line.product_id.id == self.id)
            if order_line:
                order_line.unlink()
                self.is_in_order = False
        if res_model == 'purchase.order':
            order_line = self.order_po_id.order_line.filtered(lambda line: line.product_id.id == self.id)
            if order_line:
                order_line.unlink()
                self.is_in_order = False

    def action_remove_products_from_order(self):
        res_model = dict(self.env.context or {}).get('product_catalog_order_model')
        product_ids = self.env.context.get('active_ids', [])
        self.is_in_order = False
        for product_id in product_ids:

            if res_model == 'sale.order':
                order_line = self.order_id.order_line.filtered(lambda line: line.product_id.id == product_id)
                if order_line:
                    order_line.unlink()
            if res_model == 'purchase.order':
                order_line = self.order_po_id.order_line.filtered(lambda line: line.product_id.id == product_id)
                if order_line:
                    order_line.unlink()

        return True

    def action_add_qty(self):
        res_model = dict(self.env.context or {}).get('product_catalog_order_model')
        if res_model == 'sale.order':
            order_line = self.order_id.order_line.filtered(lambda line: line.product_id.id == self.id)
            order_line.product_uom_qty += 1
        if res_model == 'purchase.order':
            order_line = self.order_po_id.order_line.filtered(lambda line: line.product_id.id == self.id)
            order_line.product_qty += 1



    def action_sub_qty(self):
        res_model = dict(self.env.context or {}).get('product_catalog_order_model')
        if res_model == 'sale.order':
            order_line = self.order_id.order_line.filtered(lambda line: line.product_id.id == self.id)
            order_line.product_uom_qty -= 1
        if res_model == 'purchase.order':
            order_line = self.order_po_id.order_line.filtered(lambda line: line.product_id.id == self.id)
            order_line.product_qty -= 1



