from datetime import timedelta,date
from odoo import fields,models,api




class HomeUsers(models.Model):
    _name = "home.users"
    
    _description = "users list"
    
    
    name = fields.Char(string = 'User Name', required = True , copy = False)
    age = fields.Integer(string = "Age" ,required = True)
    expense_id = fields.Many2one('home.expense',string = "expenses")
    
    
    
    
    