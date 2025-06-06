/** @odoo-module */
    
    
import { _t } from "@web/core/l10n/translation";
import { Component, useState, reactive } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Dialog } from "@web/core/dialog/dialog";



export class ProductDetailsPopup extends Component {
    static template = "sh_pos_motorcycle.ProductDetailsPopup";
    static components = { Dialog };
    
        setup() {
            super.setup();
            this.pos = usePos();
        } 
    }
