from odoo import models,fields


#estate property  type  model
#many to one relationship with estate property model 
class EstatePropertyTypeEight(models.Model):
    _name = "estate.property.type.eight"
    _description = "type of estate properties for module eight"
    
    name = fields.Char(string = "property Type",required = True)
    
    
    