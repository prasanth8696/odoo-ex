from odoo import models,fields


#estate property model
class EstatePropertyFour(models.Model):
    _name = 'estate.property.four'
    _description = 'estate property model four'
    
    
    name = fields.Char(required = True)
    description = fields.Text()
    post_code = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection = [('east','East'),('west','West'),('north','North'),('south','South')]) # (value,label)
    
    
    
    
    
    
    

  