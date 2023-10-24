from odoo import models, fields, _

class AmericadigitalMayorista(models.Model):
    _name = 'americadigital.mayorista'
    _description = 'Mayorista'
    
    name = fields.Char('Nombre')
