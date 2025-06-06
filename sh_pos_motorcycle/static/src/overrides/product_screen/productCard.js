import { _t } from '@web/core/l10n/translation';
import { patch } from '@web/core/utils/patch';
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { makeAwaitable } from "@point_of_sale/app/store/make_awaitable_dialog";
import { ProductDetailsPopup } from "@sh_pos_motorcycle/apps/popups/ProductDetailsPopup";
import { useService } from "@web/core/utils/hooks";


patch(ProductCard.prototype, {
    setup() {
        super.setup(...arguments);
        this.dialog = useService("dialog");

    },
    async ClickOnDetails(event, Product) {
        event.stopPropagation()
        console.log(Product);
        
        var motorcycle_ids = Product.motorcycle_ids

        // var details = []

        // for (const each_motorcycle of motorcycle_id) {
        //     var res = self.pos.db.get_motorcycle_by_id(each_motorcycle)
        //     details.push(res)
        // }\
        console.log('motorcycle_ids--->',this);
        
        const label = await makeAwaitable(this.dialog, ProductDetailsPopup, {
            details: motorcycle_ids,
            title: 'Details'
          });
        if (label) {
        } else {
            return;
        }

    }
});
