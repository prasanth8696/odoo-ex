from odoo import fields,models


class UsersFifteen(models.Model):
    _inherit = 'res.users'
    
    property_ids = fields.One2many("estate.property.fifteen",'sales_person',string="")
    