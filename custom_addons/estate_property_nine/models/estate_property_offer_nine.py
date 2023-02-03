from datetime import date,timedelta
from odoo import api,models,fields



class EstatePropertyOfferNine(models.Model):
    _name = "estate.property.offer.nine"
    _description = "offer model for chapter nine"
    
    price = fields.Float(string = "price")
    validity = fields.Integer(string = "Validity(days)" , default = 7)
    dead_line = fields.Date(string = "Dead Line",compute = "_compute_validity_date",inverse = "_inverse_validity_date")
    status = fields.Selection(string = "status",selection = [("accepted","Accepted"),("refused","Refused")],copy = False)
    partner_id = fields.Many2one("res.partner",string = "Partner" , required = True)
    property_id = fields.Many2one("estate.property.nine",string = "Property" , required = True)
    
     
     
     
    @api.depends("validity") 
    def _compute_validity_date(self):
         
        for record in self :
            record.dead_line = (record.create_date.date()) + timedelta(days = record.validity)
             
            
    def _inverse_validity_date(self) :
        for record in self :
                record.validity = (record.dead_line - record.create_date.date()).days #inverse the filed's dependancies... 
             
 
             
            
            
            
            
            
            
            
            
            