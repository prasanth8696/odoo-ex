from odoo import fields,models,api,_
from datetime import timedelta,date
from odoo.exceptions import UserError



class MyOrders(models.Model):
    _name = "my.orders"
    _description ="order model"
    
    order_id = fields.Char(string = "Order Id" , readonly = True)
    quantity = fields.Integer(string="Quantity", required = True, copy = "False" , default = 2)
    total_amt = fields.Float(string="Total amt",compute = "_compute_total_amt")
    product_id = fields.Many2one("my.product",string="product",required=True)
    status = fields.Selection(
        string="Status",
        selection=[
            ("confirmed", "Confirmed"),
            ("shipped", "Shipped"),
            ("canceled", "Canceled"),
            ("delivered", "Delivered"),
        ],
        default="confirmed",
        store=True,
    )
    customer = fields.Many2one( "res.partner",string = "customer" ,required = True,copy = False)
    creation_date = fields.Date(string = "Ordered Date",default = date.today())
    expected_date = fields.Date(string = "Expected Date" ,compute="_compute_expected_date")
    delivery_date = fields.Date(string = "Delivery date" , readonly = True)
    
    @api.depends("product_id","quantity")
    def _compute_total_amt(self):
        for record in self :
            record.total_amt = record.quantity  * record.product_id.unit_price
            
    @api.depends("product_id")
    def _compute_expected_date(self):
        for rec in self :
            rec.expected_date = rec.creation_date + timedelta(days=rec.product_id.delivery_days)
             
            

    @api.model 
    def create(self,vals):
        vals['order_id'] = "SO/" + "{:05d}".format(1)
        
        return super(MyOrders,self).create(vals)


    def ship_order(self):
        if self.status == 'confirmed' :
            self.status = 'shipped'
        else :
            raise UserError(_(f'you cannot ship product in {self.status} state'))
    
    def cancel_order(self):
        if self.status == 'confirmed' :
            self.status = 'canceled'
        else :
            raise UserError(_(f'you cannot cancel product in {self.status} state'))
        
    def make_deliver(self):
        if self.status == 'shipped' :
            self.status = 'delivered'
            self.delivery_date = date.today()
        else :
            raise UserError(_(f'you cannot deliver a  product in {self.status} state'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        