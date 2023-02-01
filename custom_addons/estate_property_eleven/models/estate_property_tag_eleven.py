from odoo import models, fields


# estate property tag model
# many to many relationship with estate property model


class EstatePropertyTagEleven(models.Model):
    _name = "estate.property.tag.eleven"
    _description = "estate property tags for chapter eleven"
    name = fields.Char(string="Tag name", required=True)
    
    _sql_constraints = [
            ("unique_tag_name","UNIQUE(name)","tag name must unique")
]
