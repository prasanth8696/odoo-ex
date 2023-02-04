from odoo import fields,models


class UsersThirteen(models.Model):
    _inherit = 'res.users'
    
    property_ids = fields.One2many("estate.property.thirteen",'sales_person',string="")
    