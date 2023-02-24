from datetime import datetime
from datetime import date 
from dateutil.relativedelta import relativedelta
from odoo.osv import osv
from odoo import api, fields, models
from odoo import exceptions, _
from odoo.exceptions import UserError, ValidationError
import xlwt
import io
import base64
import re
import xlsxwriter
from itertools import count
from email.policy import default


class real_estate_report_wzd(models.Model):
    _name = "realestate.report"
       
    start_date = fields.Date('Date From') 
    end_date = fields.Date(string="Date To") 
    company_id = fields.Many2one('res.company',string='Company')
   
    def print_realestate_report(self):
       

        def get_lines(self):
            res = {}
            
            
            start_date = self.start_date
            end_date = self.end_date
            company_id = self.company_id.name
            
            
            
            
            sql='''
                   select c.name as name,pt.name as property_type_id,p.name as buyer_id,rp.name  as salesman_id,c.selling_price as selling_price,c.date_availability as date from advanced_chapter as c
                   join advanced_chapter_property_type as pt on c.property_type_id=pt.id
                   join res_partner as p on c.buyer_id=p.id
                   join res_users as u on c.salesman_id=u.id
                   join res_partner as rp on u.partner_id=rp.id
                    where c.create_date::date >= '%s' and c.create_date::date <='%s'
                 '''  %(start_date, end_date)
                    
                    
            self.env.cr.execute(sql)
            print(sql)
            realestate_data = self.env.cr.dictfetchall()
            if not realestate_data:
                    raise UserError(_('No data available for the input specified search criteria'))
            return realestate_data
    
       
      
        real_estate_line = []
   
        for line in get_lines(self):
            print('line',line)

            #bill_cnt+=line['INT_totalbillcount']
           # online_cnt+=line['INT_onlinecount']
           # offline_cnt+=line['INT_offlinecount']
           # cancel_cnt+=line['INT_cancelcount']
         
#             if line['delivered_qty']:
#                 dlry_qty+=line['delivered_qty']
#                          
            real_estate_line.append((0,0,{
                                 'property_name' : line['name'],
                                'property_type' : line['property_type_id'],
                                'buyer' :line['buyer_id'], 
                                'seller' : line['salesman_id'],
                                'selling_price' : line['selling_price'],
                                 'date':line['date'],
                           
                                
                                     }))
#         if real_estate_line:
#             real_estate_line.append((0,0,{
#                                     'property_name' : name,
#                                     'property_type' : property_type_id,
#                                     'buyer' :buyer_id, 
#                                     'seller' : salesman_id,
#                                     'selling_price' : selling_price,
#                                     'date':date,
#                                 }))    
                            
         
        vals = {
                #'name': 'Beat outstanding Report',
                'start_date':self.start_date ,   
                'end_date':self.end_date ,             
                'company_id':self.company_id.name , 
#                  'customer_type_title':'TYPE: ',             
#                  'customer_type': self.customer_type,date_availability
                'real_estate_line': real_estate_line,
                #'visible':True,            
                }
        
        
                
            
        real_estate_reports_id = self.env['real.estate.report.wzd'].create(vals)

        res = self.env['ir.model.data'].check_object_reference(
                                            'real_estate_report', 'view_real_estate_report')
        return {
                    'name': 'Real Estate Report',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'real.estate.report.wzd',
                    'domain': [],
                    'type': 'ir.actions.act_window',
                    'target': 'current',
                    'res_id': real_estate_reports_id.id,
            }
       
class realestate_screen_wzd(models.Model):
    _name = "real.estate.report.wzd"
    _description = "Real Estate Reports"
    
    name=fields.Char(string="Name",default='Real Estate Report')
    real_estate_line = fields.One2many('real.estate.line','real_estate_id',string='Real Estate Line')
    start_date = fields.Date('Date From') #, required=True
    end_date = fields.Date(string="Date To")
    company_id = fields.Char(string='Company')
     
    
                 
    def print_real_estate_excel_report(self):
        filename= 'Real Estate Report.xls'
        workbook= xlwt.Workbook(encoding="UTF-8")
        style_header = xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;'
                               'font: bold on; font:height 230; align: wrap No; borders: left thin, right thin, top thin, bottom thin;')
        style = xlwt.easyxf('font:height 230; align: wrap No;borders: left thin, right thin, top thin, bottom thin;')
        header=xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;''font:height 400; align: horiz center;font:bold True;' "borders: top thin,bottom thin , left thin, right thin")
        style = xlwt.easyxf('font:height 230; align: wrap No;')
        base_style = xlwt.easyxf('align: wrap yes')
        date_style = xlwt.easyxf('align: wrap yes', num_format_str='DD-MM-YYYY')
        datetime_style = xlwt.easyxf('align: wrap yes', num_format_str='DD-MM-YYYY HH:mm:SS')
        sheet= workbook.add_sheet('Real Estate  Report')
        format6 = xlwt.easyxf('pattern: pattern solid, fore_colour light_yellow;''font:height 210,bold True;align: horiz left;'"borders: top thin,bottom thin , left thin, right thin")
        format1 = xlwt.easyxf('font: bold off, color black;\
                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color white;')
        
        
        end_date = self.end_date  or ''
        start_date = self.start_date or ''
        company_id = self.company_id or ''
            
        sheet.col(0).width = 800*5
        sheet.col(1).width = 800*5
        sheet.col(2).width = 800*5
        sheet.col(3).width = 800*5
        sheet.col(4).width = 800*5
        sheet.col(5).width = 800*5
        sheet.col(6).width = 800*5
        sheet.col(7).width = 800*5 
        sheet.write(2, 0, 'Property Name', format6)
        sheet.write(2, 1, 'Property Type', format6)
        sheet.write(2, 2, 'Buyer', format6)
        sheet.write(2 ,3, 'Seller', format6)
        sheet.write(2, 4, 'Selling Price', format6)
        sheet.write(2, 5, 'Date Availability', format6)
#         sheet.write(2, 6, 'Cancel Count', format6)
        sheet.write_merge(0, 1, 0, 6, 'Real Estate Report',header)               
        sql = '''    
                   select property_name,property_type,buyer,seller,selling_price,to_char(date,'dd/mm/yy') as date from real_estate_line        
                    where real_estate_id=(select max(real_estate_id) from real_estate_line)  
                    
                     '''
           
        self.env.cr.execute(sql)
        rows2 = self.env.cr.fetchall()
        for row_index, row in enumerate(rows2):
            for cell_index, cell_value in enumerate(row):
                cell_style = format1 
                if isinstance(cell_value, str):
                    cell_value = re.sub("\r", " ", cell_value)
                elif isinstance(cell_value,float) :
                    cell_style =  format1   
                sheet.row(row_index+1).height = 70*5
                sheet.write(row_index + 3, cell_index, cell_value,format1)
                     
        fp =io.BytesIO()
        workbook.save(fp)
        export_id = self.env['excel.extended.realestate.rep'].create({'excel_file': base64.encodestring(fp.getvalue()), 'file_name': filename})
        
        fp.seek(0)
        data = fp.read()
        fp.close()

        return{
              'view_mode': 'form',
              'res_id': export_id.id,
              'res_model': 'excel.extended.realestate.rep',
              #'view_type': 'form',
              'type': 'ir.actions.act_window',
              'context': False,
              #'target': 'new',
          
            }
        
realestate_screen_wzd()
 
class real_estate_screen_line(models.Model):
    _name = "real.estate.line"
    _description = "Real Estate"
    
    real_estate_id = fields.Many2one('real.estate.report.wzd',string='ID',ondelete='cascade')
    property_name = fields.Char(string="Property Name")
#     startno = fields.Float(string="Startno")
#     endno = fields.Float(string="Endno")
    property_type = fields.Char("Property Type")
    buyer = fields.Char(string="Buyer")
    seller = fields.Char(string="Seller")
    selling_price = fields.Float(string="Selling Price")
    date = fields.Date(string="Availability Date")
    
    
    

    
           
real_estate_screen_line()
    
     
class excel_extended_realestate_rep(models.Model):
    _name= "excel.extended.realestate.rep"
    
    name=fields.Char(string="Name",default='Download Excel Report')
    excel_file = fields.Binary('Download report Excel')
    file_name = fields.Char('Excel File', size=64) 
    
    
