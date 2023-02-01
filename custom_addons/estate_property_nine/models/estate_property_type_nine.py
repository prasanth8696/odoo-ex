from odoo import models,fields


#estate property  type  model
#many to one relationship with estate property model 
class EstatePropertyTypeNine(models.Model):
    _name = "estate.property.type.nine"
    _description = "type of estate properties for module nine"
    
    name = fields.Char(string = "property Type",required = True)
    
    
    