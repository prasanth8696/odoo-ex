from odoo import models,fields

class EstatePropertyOfferEight(models.Model):
    _name = "estate.property.offer.eight"
    _description = "offer model for chapter eight"
    
    price = fields.Float(string = "price")
    status = fields.Selection(string = "status",selection = [("accepted","Accepted"),("refused","Refused")],copy = False)
    partner_id = fields.Many2one("res.partner",string = "Partner" , required = True)
    property_id = fields.Many2one("estate.property.eight",string = "Property" , required = True)