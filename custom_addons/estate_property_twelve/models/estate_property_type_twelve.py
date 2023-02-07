from odoo import models,fields,api


# estate property  type  model
# many to one relationship with estate property model
class EstatePropertyTypeTwelve(models.Model):
    _name = "estate.property.type.twelve"
    _description = "type of estate properties for module twelve"

    name = fields.Char(string="property Type", required=True)
    property_ids = fields.One2many("estate.property.twelve","property_type_id",string = "properties",)
    offer_ids = fields.One2many("estate.property.offer.twelve","property_type_id",string = "offers")
    offer_count = fields.Integer(string = "count",compute="_compute_offer_count")
    sequence = fields.Integer(string = "Sequence" , default = 1)
    _sql_constraints = [
                ("unique_type_name","UNIQUE(name)","name must be unique"),
                ("unique_sequence_name","UNIQUE(sequence)","sequence must be unique")

]
    _order = "sequence"
    
    
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.property_ids.offer_ids)
            print(rec.offer_count)
    def show_offers(self):
        return {
             'type' : 'ir.actions.act_window',
             'name' : 'Offers',
             'res_model' : 'estate.property.offer.twelve',
             'view_mode' : 'tree,form',
              'target' : 'current',
              'context': "{'create': False}",
              
             }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    