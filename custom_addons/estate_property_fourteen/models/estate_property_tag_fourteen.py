from odoo import models, fields


# estate property tag model
# many to many relationship with estate property model


class EstatePropertyTagFourteen(models.Model):
    _name = "estate.property.tag.fourteen"
    _description = "estate property tags for chapter fourteen"
    name = fields.Char(string="Tag name", required=True)
    color = fields.Integer(string = "Color")
    
    _sql_constraints = [
            ("unique_tag_name","UNIQUE(name)","tag name must unique")
    ]
    
    _order = "name"

