from odoo import fields,models,api,_
from datetime import date,timedelta
from odoo.exceptions import  UserError



class MyPurchase(models.Model):
    _name = "my.purchase"
    _description = "purchase model"
    
    product_id = fields.Many2one("my.product",string = "product")
    
    created_date = fields.Date(string = "Created date" , default = date.today())
    
    quantity = fields.Integer(string = "quantity", required = True)
    
    total_amt = fields.Float(string = "Total Amt" ,compute = "_compute_total_amt")
    
    status = fields.Selection(string = "status" ,selection=[('draft','QUOATATION'),('sent','QUOATATION SENT'),('confirm','PURCHASE ORDER'),('done','RECEIVED')],default = 'draft')
    
    
    
    
    @api.depends("product_id","quantity")
    def _compute_total_amt(self):
        for rec in self :
            rec.total_amt = rec.product_id.original_price * rec.quantity
            
    @api.onchange("status")
    def onchange_quantity(self):
        if self.status == 'done' :
            product = self.env["my.product"].browse(self.product_id.id)
         
            product.avail_quantity += vals['quantity']
            
            
#     @api.model 
#     def create(self,vals):
#         product = self.env["my.product"].browse(self.product_id.id)
#         
#         product.quantity += vals[quantity]
#         
#         return super(MyPurchase,self).create(vals)
 
    
    def send(self):
        if self.status in ('draft','sent'):
            self.status = 'sent'
        else :
            raise UserError(_('quoatation already sent...'))
    def confirm(self):
        if self.status in ('draft','sent') :
            self.status = 'confirm'
        else :
            raise UserError(_("purchase aleady confirmed..."))

    def received_products(self):
        if self.status == 'confirm' :
            self.status = 'done'
        else :
            raise UserError(_("oder not yet confirmed..."))
     
    