from odoo import fields,models



class HomeExpense(models.Model):
    _name = 'home.expense'
    
    _description = 'expense model'
    
    
    name = fields.Char(string = "Title",required = True)
    decription = fields.Char(string = "Description")
    creation_date = fields.Date(string = "Created Date",  default=date.today(),readonly = True)
    Author = fields.Many2one('home.users',string = "Paid By" ,required = True)
    user_ids = fields.Many2many('home.users',string = "total Users",required = True)
    payment_lines = fields.One2many('payment.lines','expense_id')