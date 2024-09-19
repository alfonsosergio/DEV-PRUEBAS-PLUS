from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'
    _description = 'Mi primer modelo'

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')