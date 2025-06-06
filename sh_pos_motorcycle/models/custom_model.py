# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api

class motorcycletype(models.Model):
    _inherit = 'motorcycle.type'

    @api.model
    def _load_pos_data_domain(self, data):
        return [ ]
    
    @api.model
    def _load_pos_data_fields(self, config_id):
        return [ ]
    
    def _load_pos_data(self, data):
        domain = self._load_pos_data_domain(data)
        fields = self._load_pos_data_fields(data['pos.config']['data'][0]['id'])
        return {
            'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            'fields': fields,
        }

class motorcyclemake(models.Model):
    _inherit = 'motorcycle.make'

    @api.model
    def _load_pos_data_domain(self, data):
        return [ ]
    
    @api.model
    def _load_pos_data_fields(self, config_id):
        return [ ]
    
    def _load_pos_data(self, data):
        domain = self._load_pos_data_domain(data)
        fields = self._load_pos_data_fields(data['pos.config']['data'][0]['id'])
        return {
            'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            'fields': fields,
        }
    
class Motorcycalemodel(models.Model):
    _inherit = "motorcycle.mmodel"

    def _load_pos_data(self, data):
        domain = []
        fields = []
        return {
            'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            'fields': fields,
        }

class Motorcycaleyear(models.Model):
    _inherit = "motorcycle.year"

    def _load_pos_data(self, data):
        domain = []
        fields = []
        return {
            'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            'fields': fields,
        }

class motorcyclemotorcycle(models.Model):
    _inherit = "motorcycle.motorcycle"

    def _load_pos_data(self, data):
        domain = []
        fields = []
        return {
            'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            'fields': fields,
        }
    

class productproduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        fields += ['sh_is_common_product','motorcycle_ids']
        return fields