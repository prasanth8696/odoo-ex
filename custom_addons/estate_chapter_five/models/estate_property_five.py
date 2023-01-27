from odoo import models,fields


#estate property model
class EstatePropertyFive(models.Model):
    _name = 'estate.property.five'
    _description = 'estate property model five'
    
    
    name = fields.Char(string = 'Name',required = True)
    description = fields.Text(string = 'Description' )
    post_code = fields.Char(string = 'PostCode' )
    date_availability = fields.Date(string = 'DateAvailability' )
    expected_price = fields.Float(string = 'ExpectedPrice', required = True)
    selling_price = fields.Float(string = 'SellingPrice' )
    bedrooms = fields.Integer(string = 'Bedrooms')
    living_area = fields.Integer(string = 'LivingArea')
    facades = fields.Integer(string = 'Facades')
    garage = fields.Boolean(string = 'Garage')
    garden = fields.Boolean(string = 'Garden' )
    garden_area = fields.Integer(string = 'garden_area' )
    garden_orientation = fields.Selection(string = 'GardenOrientation',selection = [('east','East'),('west','West'),('north','North'),('south','South')]) # (value,label)
    
    
    
    
    
    
    

  