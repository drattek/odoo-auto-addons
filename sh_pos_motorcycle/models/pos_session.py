# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields, api

class PosSessionInherit(models.Model):
    _inherit = "pos.session"


    @api.model
    def _load_pos_data_models(self, config_id):
        data = super()._load_pos_data_models(config_id)
        data += ['motorcycle.type','motorcycle.make', 'motorcycle.mmodel','motorcycle.year', 'motorcycle.motorcycle']
        return data
