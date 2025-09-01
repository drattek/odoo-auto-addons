# -*- coding: utf-8 -*-
from odoo import models, api


class ProductAvailability(models.Model):
    _name = 'product.availability.catalog'
    _description = 'Product Availability Across Warehouses (Catalog)'

    @api.model
    def get_warehouses_availability(self, product_id):
        """
        Get availability of a product across all warehouses (available and forecasted)
        Returns list of dicts: [{warehouse_id, warehouse_name, available_qty, forecasted_qty}, ...]
        """
        if not product_id:
            return []

        product = self.env['product.product'].browse(product_id)
        if not product.exists():
            return []

        query = """
            SELECT 
                sq.product_id, 
                sl.warehouse_id,
                sw.name as warehouse_name,
                SUM(sq.quantity) as quantity,
                SUM(sq.reserved_quantity) as reserved_quantity
            FROM 
                stock_quant sq
            JOIN 
                stock_location sl ON sq.location_id = sl.id
            JOIN 
                stock_warehouse sw ON sl.warehouse_id = sw.id
            WHERE 
                sq.product_id = %s
                AND sl.usage = 'internal'
            GROUP BY 
                sq.product_id, sl.warehouse_id, sw.name
            ORDER BY 
                sw.name
        """

        self.env.cr.execute(query, (product_id,))
        quants_data = self.env.cr.dictfetchall()

        warehouses = self.env['stock.warehouse'].search([], order='name')

        availability_data = []
        warehouse_ids_with_data = set()

        for quant in quants_data:
            warehouse_id = quant['warehouse_id']
            warehouse_ids_with_data.add(warehouse_id)

            virtual_available = product.with_context(warehouse=warehouse_id).virtual_available

            availability_data.append({
                'warehouse_id': warehouse_id,
                'warehouse_name': quant['warehouse_name'],
                'available_qty': (quant['quantity'] or 0) - (quant['reserved_quantity'] or 0),
                'forecasted_qty': virtual_available,
            })

        for warehouse in warehouses:
            if warehouse.id not in warehouse_ids_with_data:
                availability_data.append({
                    'warehouse_id': warehouse.id,
                    'warehouse_name': warehouse.name,
                    'available_qty': 0,
                    'forecasted_qty': product.with_context(warehouse=warehouse.id).virtual_available,
                })

        return availability_data
