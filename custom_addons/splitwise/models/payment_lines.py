from odoo import fields,models


class Paymentlines(models.Model):
    _name = "payment.lines"
    
    _description = "payment_lines"
    
    
    price = fields.Float(string = "Price",required = True)
    user_id = fields.Many2one("home.users",string = "User",required = True )
    status = fields.Selection(string = "status" , selection = [('not_paid','Not Paid'),('processing','Processing')('paid','Paid')],default = 'not_paid') 
    