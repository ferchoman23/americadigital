from odoo import models, fields, _

class AmericadigitalImportador(models.Model):
    _name = 'americadigital.importador'
    _description = 'Importador'
	
    name = fields.Char('Nombre')
