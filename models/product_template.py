from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    distribuidor_id = fields.Many2one('americadigital.distribuidor', 'Distribuidor')
    importador_id = fields.Many2one('americadigital.importador', 'Importador')
    mayorista_id = fields.Many2one('americadigital.mayorista', 'Mayorista')
