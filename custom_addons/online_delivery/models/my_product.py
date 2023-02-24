from odoo import fields,models,api



class MyProduct(models.Model):
    _name = "my.product"
    _description ="product model"
    
    
    name = fields.Char(string = "Product Name" , required = True)
    category_id = fields.Many2one("my.categories",string = "Category")
    sequence = fields.Integer(string = "Sequence")
    order_ids= fields.One2many('my.orders','product_id' ,string = "Orders")
    avail_quantity = fields.Integer(string="Available Quantity")
    original_price = fields.Float(string = "Original price")
    unit_price = fields.Float(string = "Sales Price" , required = True)
    delivery_days = fields.Integer(string = "Delivery Days", default = 10)
    purchase_ids = fields.One2many("my.purchase",'product_id')
    
    
    
    
    
    
        
    