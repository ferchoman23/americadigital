from odoo import models, fields, _

class AmericadigitalDistribuidor(models.Model):
    _name = 'americadigital.distribuidor'
    _description = 'Distribuidor'
    
    name = fields.Char('Nombre')
