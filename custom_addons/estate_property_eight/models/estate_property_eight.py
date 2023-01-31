from odoo import models,fields
from datetime import date
from dateutil.relativedelta import relativedelta


#estate property model
class EstatePropertyEight(models.Model):
    _name = 'estate.property.eight'
    _description = 'estate property model eight'
    
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
    property_type_id = fields.Many2one("estate.property.type.eight",string = "Property Type",required=True)
    sales_person = fields.Many2one("res.users",string = "Sales person",default = lambda self : self.env.user )
    buyer = fields.Many2one("res.partner",string="Buyer",copy=False)
    tag_ids = fields.Many2many("estate.property.tag.eight",string = "tags" )
    
    offer_ids = fields.One2many("estate.property.offer.eight","property_id",string = "Offer")
    
    
    
  
    
    

  