from odoo import fields,models



class CancelModelWizard(models.TransientModel):
    _name = "cancel.model.wizard"
    _description = "for cancel popup"
    
    
    reason = fields.Char(string="what is the reason", required = True)
    
    
    
    def submit_wizard(self):
        id = self.env.context.get('property_id')
        property = self.env["estate.property.fifteen"].browse(id)
        property.cancel_property(self.reason) # call the cancel property in particular recor...
       