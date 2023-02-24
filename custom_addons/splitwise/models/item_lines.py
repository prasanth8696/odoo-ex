from odoo import fields,models


class ItemLines(models.Model):
    
    _name = "item.lines"
    _description = "item lines"
    
    
    name = fields.Char(string = "Item Name",required = True)
    price = fields.Float(string = "Price" , required = True)
    quantity = fields.Integer(string = 'Quantity' ,default = 1)
    total_amt = fields.Float(string = 'Total Amt' ,compute = "_compute_total_amt")
    expense_id = fields.Many2one("home.expense")
    
    
    
    
    @api.depends("quantity")
    def _compute_total_amt(self):
        for rec in  self :
            rec.total_amt = rec.price * quantity 
            
    