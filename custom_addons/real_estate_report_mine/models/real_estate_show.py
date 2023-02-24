from odoo import fields,models
import xlwt
import io
import base64
import re
import xlsxwriter



class RealEstateShow(models.Model):
    _name  = "real.estate.show"
    _description = "display report screen"
    
    
    name = fields.Char(string = "Name" , default = 'Real Estate Report')
    estate_line_ids = fields.One2many('real.estate.line','estate_id',string='')
    start_date = fields.Date('Date From')
    end_date = fields.Date(string="Date To")
    property_type_id = fields.Many2one("estate.property.type.fifteen", string = "Property Type")
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
    
    
    def print_excel_report(self):
        filename  = 'Real Estate Report.xls'
        workbook= xlwt.Workbook(encoding="UTF-8")
        style_header = xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;'
                               'font: bold on; font:height 230; align: wrap No; borders: left thin, right thin, top thin, bottom thin;')
        style = xlwt.easyxf('font:height 230; align: wrap No;borders: left thin, right thin, top thin, bottom thin;')
        header=xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;''font:height 400; align: horiz center;font:bold True;' "borders: top thin,bottom thin , left thin, right thin")
        style = xlwt.easyxf('font:height 230; align: wrap No;')
        base_style = xlwt.easyxf('align: wrap yes')
        date_style = xlwt.easyxf('align: wrap yes', num_format_str='DD-MM-YYYY')
#       datetime_style = xlwt.easyxf('align: wrap yes', num_format_str='DD-MM-YYYY HH:mm:SS')
        sheet= workbook.add_sheet('Real Estate  Report')
        format6 = xlwt.easyxf('pattern: pattern solid, fore_colour light_yellow;''font:height 210,bold True;align: horiz left;'"borders: top thin,bottom thin , left thin, right thin")
        format1 = xlwt.easyxf('font: bold off, color black;\
                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color white;')
        
        
#         end_date = self.end_date  or ''
#         start_date = self.start_date or ''
#         company_id = self.company_id or ''
            
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
                  
           
#         SQL_QUERY = f'''select e.name as Title,t.name as PropertyType,b.name as Buyer,r.id,e.selling_price as SellingPrice,to_char(e.date_availability,'dd/mm/yy') as Date from estate_property_fifteen as e join estate_property_type_fifteen as t on e.property_type_id = t.id
#                       left join res_partner as b on b.id = e.buyer join res_users as r on r.id = e.sales_person where t.id = {self.property_type_id.id};
# '''
        
        SQL_QUERY = '''select property_name,property_type,buyer,seller,selling_price,to_char(date,'dd/mm/yy') as date from real_estate_line 
                      where estate_id = (select max(estate_id) from real_estate_line);'''
        self.env.cr.execute(SQL_QUERY)
        rows = self.env.cr.fetchall()
        
        for r in rows :
            print(r)
        for row_index, row in enumerate(rows):
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
        current_excel_id = self.env['excel.report'].create({'excel_file': base64.encodestring(fp.getvalue()), 'file_name': filename})
        
        fp.seek(0)
        data = fp.read()
        fp.close()
        
        sql = f" DELETE from excel_report where id != {current_excel_id.id}"
        
        self.env.cr.execute(sql)

        return{
              'view_mode': 'form',
              'res_id': current_excel_id.id,
              'res_model': 'excel.report',
              'view_type': 'form',
              'type': 'ir.actions.act_window',
              'context': False,
          }
            
    
    
    
    
    def print_pdf_report(self):
                return self.env.ref('real_estate_report_mine.real_estate_report').report_action(self)

  