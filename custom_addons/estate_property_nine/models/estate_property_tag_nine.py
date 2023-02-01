from odoo import models,fields


#estate property tag model
#many to many relationship with estate property model

class EstatePropertyTagNine(models.Model):
    _name = "estate.property.tag.nine"
    _description = "estate property tags for chapter nine"
    name = fields.Char(string = "Tag name" , required = True)