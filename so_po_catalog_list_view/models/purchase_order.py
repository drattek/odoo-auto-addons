from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_add_from_catalog(self):
        #Add the product's tree view .
        action = super().action_add_from_catalog()
        tree_view_id = self.env.ref('so_po_catalog_list_view.product_view_tree_catalog').id
        action['views'][0] = (tree_view_id, 'list')
        return action