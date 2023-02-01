from odoo import models, fields


# estate property  type  model
# many to one relationship with estate property model
class EstatePropertyTypeEleven(models.Model):
    _name = "estate.property.type.eleven"
    _description = "type of estate properties for module eleven"

    name = fields.Char(string="property Type", required=True)
    
    _sql_constraints = [
                ("unique_type_name","UNIQUE(name)","name must be unique")
]
