from odoo import fields,models


class UsersFourteen(models.Model):
    _inherit = 'res.users'
    
    property_ids = fields.One2many("estate.property.fourteen",'sales_person',string="")
    