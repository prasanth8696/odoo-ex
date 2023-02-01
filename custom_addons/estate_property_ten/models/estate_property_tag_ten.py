from odoo import models, fields


# estate property tag model
# many to many relationship with estate property model


class EstatePropertyTagTen(models.Model):
    _name = "estate.property.tag.ten"
    _description = "estate property tags for chapter ten"
    name = fields.Char(string="Tag name", required=True)
