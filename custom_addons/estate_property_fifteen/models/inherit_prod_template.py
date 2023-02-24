from odoo import fields,models



class InheritProdTemplate(models.Model) :
	_inherit = "product.template"

	property_tag_ids = fields.Many2many("estate.property.tag.fifteen",string = "Property Tags")
