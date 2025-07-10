/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ListRenderer } from "@web/views/list/list_renderer";

patch(ListRenderer.prototype, {
    setup() {
        super.setup(...arguments);
    },

    getActiveColumns(list) {
        let activeColumns = super.getActiveColumns(list);
        
        const warehouseAvailabilityColumns = this.allColumns.filter(
            (col) => col.name === 'show_warehouse_availability'
        );
        
        if (warehouseAvailabilityColumns.length > 0) {
            const warehouseColumn = warehouseAvailabilityColumns[0];

            const isWarehouseColumnHidden = warehouseColumn.optional === 'hide' && 
                !activeColumns.some(col => col.name === 'show_warehouse_availability');

            if (isWarehouseColumnHidden) {
                activeColumns = activeColumns.filter(col => 
                    col.name !== 'show_warehouse_availability' && 
                    col.name !== 'qty_at_date_purchase_widget' &&
                    col.name !== 'qty_at_date_widget'
                );
            }
        }
        
        activeColumns = activeColumns.filter(col => col.name !== 'show_warehouse_availability');
        return activeColumns;
    }
});
