from odoo import models, fields, api

class Lunch(models.Model):
    _name = 'lunch.lunch'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
