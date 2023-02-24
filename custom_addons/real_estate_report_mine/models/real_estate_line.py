from odoo import fields,models



class RealEstateLines(models.Model):
    _name = "real.estate.line"
    
    
    
    estate_id = fields.Many2one('real.estate.show',string = 'ID',ondelete = 'cascade')
    property_name = fields.Char(string = "Property Name")
    property_type = fields.Char("Property Type")
    buyer = fields.Char(string="Buyer")
    seller = fields.Char(string="Seller")
    selling_price = fields.Float(string="Selling Price")
    date = fields.Date(string="Availability Date")