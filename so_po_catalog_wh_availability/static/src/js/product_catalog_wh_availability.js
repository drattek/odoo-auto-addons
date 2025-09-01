/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ListRenderer } from "@web/views/list/list_renderer";
import { useService } from "@web/core/utils/hooks";
import { onMounted, useState } from "@odoo/owl";
import { productTreeCatalogView } from "so_po_catalog_list_view/static/src/product_catalog/tree_view";

// A renderer wrapper to inject dynamic warehouse columns for the product catalog list view
class CatalogWarehouseRenderer extends ListRenderer {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.ui = useService("ui");
        this.state = useState({
            warehouses: [],
            availabilityByProduct: {},
            loaded: false,
        });

        onMounted(async () => {
            try {
                // Load warehouses
                const warehouses = await this.orm.searchRead(
                    "stock.warehouse",
                    [],
                    ["name"],
                    { order: "name" }
                );
                this.state.warehouses = warehouses;

                // For each row (product), fetch availability
                const productIds = this.props.list.records.map((r) => r.resId).filter(Boolean);
                // Minimal approach: call one by one to reuse existing single-product method
                for (const pid of productIds) {
                    try {
                        const rows = await this.orm.call(
                            "product.availability.catalog",
                            "get_warehouses_availability",
                            [pid]
                        );
                        const avByWh = {};
                        for (const rec of rows) {
                            avByWh[rec.warehouse_id] = rec;
                        }
                        this.state.availabilityByProduct[pid] = avByWh;
                    } catch (e) {
                        // ignore per-row fetch error
                        console.error("Availability fetch error for product", pid, e);
                    }
                }

                this.state.loaded = true;
                // After data is ready, inject columns
                this.injectColumns();
            } catch (e) {
                console.error("Error initializing warehouse availability:", e);
            }
        });
    }

    // Inject columns into the table header and rows (DOM manipulation minimal approach)
    injectColumns() {
        // Ensure list has been rendered
        const table = this.el?.querySelector("table.o_list_table");
        if (!table || !this.state.loaded) {
            return;
        }
        const headerRow = table.querySelector("thead tr");
        if (!headerRow) {
            return;
        }

        // Avoid duplicate injection
        if (headerRow.querySelector("th[data-wh-col='1']")) {
            return;
        }

        // Create header THs for warehouses (Available)
        for (const wh of this.state.warehouses) {
            const th = document.createElement("th");
            th.setAttribute("data-wh-col", "1");
            th.textContent = `${wh.name} (Avail)`;
            headerRow.appendChild(th);
        }

        // And forecast columns
        for (const wh of this.state.warehouses) {
            const th = document.createElement("th");
            th.setAttribute("data-wh-col", "1");
            th.textContent = `${wh.name} (Forecast)`;
            headerRow.appendChild(th);
        }

        // Append TDs for each row with values
        const bodyRows = table.querySelectorAll("tbody tr.o_data_row");
        bodyRows.forEach((tr, idx) => {
            const record = this.props.list.records[idx];
            const productId = record?.resId;
            const byWh = this.state.availabilityByProduct[productId] || {};

            // Available qty per warehouse
            for (const wh of this.state.warehouses) {
                const td = document.createElement("td");
                td.setAttribute("data-wh-col", "1");
                const rec = byWh[wh.id];
                td.textContent = rec ? String(rec.available_qty ?? 0) : "0";
                tr.appendChild(td);
            }
            // Forecasted qty per warehouse
            for (const wh of this.state.warehouses) {
                const td = document.createElement("td");
                td.setAttribute("data-wh-col", "1");
                const rec = byWh[wh.id];
                td.textContent = rec ? String(rec.forecasted_qty ?? 0) : "0";
                tr.appendChild(td);
            }
        });
    }

    // When the list re-renders (pagination, filters), re-inject columns
    mounted() {
        super.mounted?.();
        // Try to re-inject in case initial onMounted hasn't run yet
        setTimeout(() => this.injectColumns(), 0);
    }

    patched() {
        super.patched?.();
        // Re-inject after patches (e.g., sorting, paging)
        setTimeout(() => this.injectColumns(), 0);
    }
}

// Register a specific view for product_tree_catalog that uses our custom renderer
const soPoCatalogWarehouseView = {
    ...productTreeCatalogView,
    Renderer: CatalogWarehouseRenderer,
};

registry.category("views").add("product_tree_catalog", soPoCatalogWarehouseView);
