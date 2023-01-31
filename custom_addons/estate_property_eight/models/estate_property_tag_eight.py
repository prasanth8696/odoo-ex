from odoo import models,fields


#estate property tag model
#many to many relationship with estate property model

class EstatePropertyTagEight(models.Model):
    _name = "estate.property.tag.eight"
    _description = "estate property tags for chapter eight"
    name = fields.Char(string = "Tag name" , required = True)