from datetime import date
from odoo import fields,models,_
from odoo.exceptions import UserError





class RealEstateReport(models.TransientModel):
    _name = "real.estate.report"
    
    
    start_date = fields.Date(string = "Start Date", required = True)
    end_date = fields.Date(string = "Start Date", required = True ,default = date.today())
    property_type_id = fields.Many2one("estate.property.type.fifteen", string = "Property Type" , required = True )
    status = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer received", "Offer Received"),
            ("offer accepted", "Offer Accepted"),
            ("canceled", "Canceled"),
            ("sold", "Sold"),
        ],
     )
    
    
    def print_report(self):
        
        def get_lines(self):
            print(self.start_date)
            print(type(self.start_date))
#             SQL_QUERY = f''' select estate.name ,estate.buyer,estate.sales_person,estate.selling_price,type.name ,estate.date_availability from estate_property_fifteen as estate
#                         join estate_property_type_fifteen  as type on estate.property_type_id = {self.property_type_id.id} join res_users  on  {self.env.user.id} = res_users.id '''
#             
             
            SQL_QUERY =  f'''select e.name as title,e.buyer,e.sales_person,e.selling_price,t.name,e.date_availability as date  from estate_property_fifteen as e join estate_property_type_fifteen as t on e.property_type_id = t.id  join res_users as u on u.id = e.sales_person
                          left join res_partner as b on b.id = e.buyer where t.id = {self.property_type_id.id} AND  e.create_date::date BETWEEN '{self.start_date}' AND '{self.end_date}' '''
              
#                      
#             SQL_QUERY =  f'''select e.name as title,e.buyer,e.sales_person,e.selling_price,t.name,e.date_availability as date  from estate_property_fifteen as e join estate_property_type_fifteen as t on e.property_type_id = {self.property_type_id.id}  join res_users as u on u.id = e.sales_person
#                           left join res_partner as b on b.id = e.buyer where t.id = {self.property_type_id.id} and to_char (CAST(e.create_date AS date), 'DD-MM-YYYY') BETWEEN {self.start_date} and {self.end_date} '''
#              
#             
            self.env.cr.execute(SQL_QUERY)
             
            real_estate_data = self.env.cr.dictfetchall()
            
            if not real_estate_data :
                raise UserError(_("No Match Found"))
            return real_estate_data
        
        lines = []   
        for line in get_lines(self) :
            
           lines.append((0,0,{
               "property_name" : line["title"],
                "property_type" : line["name"],
                "buyer" : self.env["res.partner"].browse(line["buyer"]).name if line["buyer"] else "None",
                "seller" : self.env["res.users"].browse(line["sales_person"]).name,
                "selling_price" : line["selling_price"],
                "date" : line["date"]}))
           
           
        vals = {
            "start_date" : self.start_date,
            "end_date" : self.end_date,
            "property_type_id" : self.property_type_id.id,
            "status" : self.status,
            "estate_line_ids" : lines
            }  
        
        real_estate_report_id = self.env["real.estate.show"].create(vals)
        
        print(real_estate_report_id)
        
        SQL_QUERY_2 = f''' DELETE from  real_estate_show where id not in ({real_estate_report_id.id})  '''
        
        self.env.cr.execute(SQL_QUERY_2)
        
        return {
                    'name': 'Real Estate Report',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'real.estate.show',
                    'domain': [],
                    'type': 'ir.actions.act_window',
                    'target': 'current',
                    'res_id': real_estate_report_id.id,
            }
        
        
    
        
        
           
        
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           

    