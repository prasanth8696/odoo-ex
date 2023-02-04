from odoo import models,fields,api


# estate property  type  model
# many to one relationship with estate property model
class EstatePropertyTypeThirteen(models.Model):
    _name = "estate.property.type.thirteen"
    _description = "type of estate properties for module thirteen"

    name = fields.Char(string="property Type", required=True)
    property_ids = fields.One2many("estate.property.thirteen","property_type_id",string = "properties",)
    offer_ids = fields.One2many("estate.property.offer.thirteen","property_type_id",string = "offers")
    offer_count = fields.Integer(string = "count",compute="_compute_offer_count")
    sequence = fields.Integer(string = "Sequence" , default = 1)
    _sql_constraints = [
                ("unique_type_name","UNIQUE(name)","name must be unique"),
                ("unique_sequence_name","UNIQUE(sequence)","sequence must be unique")

]
    _order = "sequence"
    
    
    @api.depends("offer_ids")
    def _compute_offer_count(self):
  
        offers = self.env['estate.property.offer.thirteen'].browse(self.id)
        print(offers)
    
        
    def show_offers(self):
        return {
             'type' : 'ir.actions.act_window',
             'name' : 'Offers',
             'res_model' : 'estate.property.offer.thirteen',
             'view_mode' : 'tree,form',
              'target' : 'current',
              'context': "{'create': False}",
              
              
             }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    