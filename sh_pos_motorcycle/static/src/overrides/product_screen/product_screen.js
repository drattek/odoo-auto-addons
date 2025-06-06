import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

patch(ProductScreen.prototype, {
    setup() {
        super.setup(...arguments)
        this.sh_state = useState({
            searched_type: 0, searched_make: 0, searched_model: 0, searched_year: 0,
            sh_enable_search_type: false,
            sh_enable_search_make: true,
            sh_enable_search_model: true,
            sh_enable_search_year: true,
            sh_motorcycal_products: []
        });
    },
    clear_search() {
        this.sh_state.sh_motorcycal_products = []
    },
    SearchMotorcycleType(event) {
        const value = event.target.value
        var datalist = document.getElementById('motorcycle_types');
        var options = datalist.querySelectorAll('option');

        for (var i = 0; i < options.length; i++) {
            if (options[i].value === value) {
                this.sh_state.searched_type = parseInt(options[i].getAttribute('data-id'))
                this.sh_state.sh_enable_search_make = false
                break;
            }
        }
        if (value === "") {
            this.sh_state.sh_enable_search_make = true
        }
    },
    SearchMotorcycleMake(event) {
        const value = event.target.value
        var datalist = document.getElementById('motorcycle_makes');
        var options = datalist.querySelectorAll('option');

        for (var i = 0; i < options.length; i++) {
            if (options[i].value === value) {
                this.sh_state.searched_make = parseInt(options[i].getAttribute('data-id'))
                this.sh_state.sh_enable_search_model = false
                break;
            }
        }
        if (value === "") {
            this.sh_state.sh_enable_search_model = true
        }
    },
    SearchMotorcycleModel(event) {
        const value = event.target.value
        var datalist = document.getElementById('motorcycle_models');
        var options = datalist.querySelectorAll('option');
        console.log('values ---> ', datalist, options);

        for (var i = 0; i < options.length; i++) {
            console.log(options[i].value);

            if (options[i].value === value) {
                this.sh_state.searched_model = parseInt(options[i].getAttribute('data-id'))
                this.sh_state.sh_enable_search_year = false
                break;
            }
        }
        if (value === "") {
            this.sh_state.sh_enable_search_year = true
        }
    },
    SearchMotorcycleyear(event) {
        const value = event.target.value
        var datalist = document.getElementById('motorcycle_years');
        var options = datalist.querySelectorAll('option');

        for (var i = 0; i < options.length; i++) {
            console.log(options[i].value);

            if (options[i].value === value) {
                this.sh_state.searched_year = parseInt(options[i].getAttribute('data-id'))

                break;
            }
        }
        const mmodel = posmodel.models['motorcycle.motorcycle'].filter((x) => x.mmodel_id.id == this.sh_state.searched_model && x.make_id.id == this.sh_state.searched_make && x.type_id.id == this.sh_state.searched_type)

        if (mmodel) {
            var products = mmodel[0].product_ids

            if (this.pos.config.enable_common_search && this.pos.config.enable_search) {
                const filter_product = posmodel.models['product.product'].filter((p) => p.available_in_pos && p.sh_is_common_product);
                console.log('bb', filter_product);

                for (const product of filter_product) {
                    products.push(product)
                }
            }

            this.sh_state.sh_motorcycal_products = products
        }
        if (value === "") {
            this.clear_search()
        }

    },
    get sh_types() {
        return posmodel.models['motorcycle.type'].getAll()
    },
    get sh_makes() {
        return posmodel.models['motorcycle.make'].getAll()
    },
    get sh_motorcycle_mmodel() {
        if (this.sh_state.searched_type && this.sh_state.searched_make) {
            return posmodel.models['motorcycle.mmodel'].filter((x) => x.make_id.id == this.sh_state.searched_make && x.type_id.id == this.sh_state.searched_type)
        } else {
            return []
        }
    },
    get sh_motorcycle_year() {
        return posmodel.models['motorcycle.year'].getAll()
    },

    get productsToDisplay() {
        var results = super.productsToDisplay

        if (this.pos.config.enable_search) {
            console.log('====>', this.sh_state.sh_motorcycal_products);

            if (this.sh_state.sh_motorcycal_products && this.sh_state.sh_motorcycal_products.length) {
                return this.sh_state.sh_motorcycal_products
            } else {
                return results
            }
        } else {
            return results
        }

    },
    clearType_search(event) {
        this.sh_state.sh_enable_search_type = 0
        var input = document.getElementById('motorcycle_type');
        input.value = ""
        this.sh_state.sh_enable_search_make = true
        var input1 = document.getElementById('motorcycle_make');
        input1.value = ""
        this.sh_state.sh_enable_search_model = true
        var input2 = document.getElementById('motorcycle_model');
        input2.value = ""
        this.sh_state.sh_enable_search_year = true
        var inpu3 = document.getElementById('motorcycle_year');
        inpu3.value = ""
    },
    clear_make_search(event) {
        this.sh_state.sh_enable_search_make = 0
        var input = document.getElementById('motorcycle_make');
        input.value = ""
        this.sh_state.sh_enable_search_model = true
        var input1 = document.getElementById('motorcycle_model');
        input1.value = ""
        this.sh_state.sh_enable_search_year = true
        var input2 = document.getElementById('motorcycle_year');
        input2.value = ""
    },
    clearModelSearch(event) {
        this.sh_state.sh_enable_search_model = 0
        var input = document.getElementById('motorcycle_model');
        input.value = ""
        this.sh_state.sh_enable_search_year = true
        var input1 = document.getElementById('motorcycle_year');
        input1.value = ""
        this.clear_search()
    },
    clearYearSearch(event) {
        this.sh_state.sh_enable_search_year = 0
        var input = document.getElementById('motorcycle_year');
        input.value = ""
        this.clear_search()
    },
});
