/** @odoo-module **/

import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";

import { ProductTreeCatalogSearchPanel } from "./search/search_panel";

export const productTreeCatalogView = {
    ...listView,
    SearchPanel: ProductTreeCatalogSearchPanel,
};

registry.category("views").add("product_tree_catalog", productTreeCatalogView);