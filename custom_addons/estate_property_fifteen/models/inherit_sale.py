from odoo import fields,models,api
import random


class InheritSale(models.Model):
	_inherit = 'sale.order'

	property_type_id = fields.Many2one('estate.property.type.fifteen',string = "Property Type")
	
	
	def _default_property(self):
 		return self.env["estate.property.fifteen"].search([('status','=','sold')],limit=1).id
	
	
	property = fields.Many2one('estate.property.fifteen', required = True, string = "Property",default=_default_property)
							
							


	
   	
   	
   	
	
		
			








