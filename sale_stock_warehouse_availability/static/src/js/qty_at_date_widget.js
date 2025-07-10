/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";

import { QtyAtDatePopover, QtyAtDateWidget } from "@sale_stock/widgets/qty_at_date_widget";

patch(QtyAtDatePopover.prototype, {
  setup() {
    super.setup();

    this.orm = useService("orm");
    this.state = useState({
      warehouseData: [],
      warehouseDataLoaded: false,
      showWarehouseData: false,
      loading: false,
    });

  },

  toggleWarehouseData() {
    if (!this.state.warehouseDataLoaded) {
      this.loadWarehouseData()
    }
    this.state.showWarehouseData = !this.state.showWarehouseData
  },

  async loadWarehouseData() {
    this.state.loading = true
    const productId = this.props.record.data.product_id[0];

    if (!productId){
      return;
    }

    try {
      this.state.warehouseData = await this.orm.call("product.availability", "get_warehouses_availability", [productId])
      this.state.warehouseDataLoaded = true
    } 
    catch (error) {
      console.error("Error fetching warehouse availability:", error)
    } 
    finally {
      this.state.loading = false
    }
  },
});
