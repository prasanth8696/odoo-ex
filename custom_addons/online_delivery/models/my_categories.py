from odoo import fields,models,api



class MyCategories(models.Model):
    _name = "my.categories"
    _description ="category model"
    
    name = fields.Char(string ="Title",required = True,copy = False)
    sequence = fields.Integer(string = "sequence",required = True)
    product_ids = fields.One2many("my.product","category_id",string = "products")