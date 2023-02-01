from odoo import models, fields


# estate property  type  model
# many to one relationship with estate property model
class EstatePropertyTypeTen(models.Model):
    _name = "estate.property.type.ten"
    _description = "type of estate properties for module ten"

    name = fields.Char(string="property Type", required=True)
