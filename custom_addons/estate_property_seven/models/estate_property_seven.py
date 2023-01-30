from odoo import models,fields
from datetime import date
from dateutil.relativedelta import relativedelta


#estate property model
class EstatePropertySeven(models.Model):
    _name = 'estate.property.seven'
    _description = 'estate property model seven'
    
    name = fields.Char(string = 'Title',required = True)
    description = fields.Text(string = 'Description' )
    post_code = fields.Char(string = 'PostCode' )
    date_availability = fields.Date(string = 'Available From',copy = False,default = date.today() + relativedelta(months = 3)) #add default value 
    expected_price = fields.Float(string = 'Expected Price', required = True)
    selling_price = fields.Float(string = 'Selling Price',readonly = True,copy = False)# copy = false >>> prevent dublicate value
    bedrooms = fields.Integer(string = 'Bedrooms',default = 2)
    living_area = fields.Integer(string = 'Living Area (sqm)') 
    facades = fields.Integer(string = 'Facades')
    garage = fields.Boolean(string = 'Garage')
    garden = fields.Boolean(string = 'Garden' )
    garden_area = fields.Integer(string = 'Garden Area' )
    garden_orientation = fields.Selection(string = 'GardenOrientation',selection = [('east','East'),('west','West'),('north','North'),('south','South')]) # (value,label)
    status = fields.Selection(string = 'Status',selection = [('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('canceled','Canceled')], default='new', store=True)
    active = fields.Boolean('active',default = True)
  
    
    

  