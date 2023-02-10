from odoo import fields,models



class EstatePropertyAccount(models.Model):
    _inherit = "estate.property.fifteen" #change accordingly for chapter
    
    #override
    def sold_property(self):
        print(" reached ".center(100, '='))
        res = super().sold_property()
        self.env["account.move"].sudo().create(
            {
                "partner_id" : self.buyer.id,
                "move_type" : "out_invoice",
                "journal_id" : 1,
                "invoice_line_ids" : [(0,0,{
                    "name" : self.name,
                    "quantity" : 1,
                    "price_unit": self.selling_price * (6/100) 
                    }
                    ),
                    (0,0,{
                    "name" : "administrative fees",
                    "quantity" : 1,
                    "price_unit": 100 #administrative fees 
                    }
                    )
                    
                ]
                
            }
        )        
        return res