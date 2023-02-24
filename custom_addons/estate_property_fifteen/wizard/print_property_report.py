import io
import xlwt
import base64
from odoo import fields,models




class PrintPropertyReport(models.TransientModel):
    _name = "print.property.report"
    
    _description = 'for property card report'
    
    
    name = fields.Char(string = "Title",default = "Property Offer Report")
    
    
    
    
    def print_pdf(self):
        id = self.env.context.get("property_id")
        
        property = self.env["estate.property.fifteen"].browse(id)
        
        return self.env.ref("estate_property_fifteen.action_report_offers").report_action(property)
        
    
    def print_excel_2(self):
        id = self.env.context.get("property_id")
        property = self.env["estate.property.fifteen"].browse(id)
        
        
        
        
        book = xlwt.Workbook(encoding="UTF-8")
        date_style = xlwt.easyxf('align: wrap yes', num_format_str='DD-MM-YYYY')
        header=xlwt.easyxf('pattern: pattern solid, fore_colour light_orange;''font:height 400; align: horiz center;font:bold True;' "borders: top thin,bottom thin , left thin, right thin")
        format6 = xlwt.easyxf('pattern: pattern solid, fore_colour light_yellow;''font:height 210,bold True;align: horiz left;'"borders: top thin,bottom thin , left thin, right thin")
        format1 = xlwt.easyxf('font: bold off, color black;\
                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color white;')
         
        temp = 5
        sheet = book.add_sheet("property Offer Report")
         
        sheet.col(0).width = 800 * 5
        sheet.col(1).width = 800 * 5
        sheet.col(2).width = 800 * 5
        sheet.col(3).width = 800 * 5
        sheet.col(4).width = 800 * 5
        sheet.col(5).width = 800 * 5
        sheet.col(6).width = 800 * 5
        sheet.col(7).width = 800 * 5 
        sheet.col(8).width = 800 * 5
         
        sheet.write_merge(0,1,0,7,"Property Offer  Report",header) # r1,r2,c1,c2 parameters
         
        sheet.write_merge(6,7,0,4,property.name,header)
         
        sheet.write(8,0,"Sales Person",format6)
        sheet.write(8,1,property.sales_person.name,format1)
        sheet.write(9,0,"Expected Price",format6)
        sheet.write(9,1,property.expected_price,format1)
        sheet.write(10,0,"Status",format6)
        sheet.write(10,1,property.status,format1)
        sheet.write(12,0,"Price",format6)
        sheet.write(12,1,"Partner",format6)
        sheet.write(12,2,"Validity(days)",format6)
        sheet.write(12,3,"Deadline",format6)
        sheet.write(12,4,"state",format6)

         
        offers = self.env["estate.property.offer.fifteen"].search([('property_id','=',id)])
        print(offers)
        row = 13
        for offer in offers :
            sheet.write(row,0,offer.price,format1)
            sheet.write(row,1,offer.partner_id.name,format1)
            sheet.write(row,2,offer.validity,format1)
            sheet.write(row,3,offer.dead_line,date_style)
            sheet.write(row,4,offer.status)
            
            row += 1
        
#         sheet.write_merge(20,20,0,10,'Hello python',header)   
        bin =io.BytesIO()
        book.save(bin)
        
        res_id = self.env['excel.report'].create({'excel_file': base64.encodestring(bin.getvalue()),'file_name' : "property offer report.xls" })
            
        
       
        return{
              'view_mode': 'form',
              'res_id': res_id.id,
              'res_model': 'excel.report',
              'type': 'ir.actions.act_window',
              'context': False,
              'target': 'new',
            }
            
        
    def print_excel(self):
        id = self.env.context.get("property_id")
        property = self.env["estate.property.fifteen"].browse(id)
        
        
        book = xlwt.Workbook()
        
        #styles
        header = xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on; align: horiz center ,vert center;'  "borders: top thin, bottom thin, left thin ,right thin;")
        format_1 = xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;'  "borders:  left thin,right thin;")
        format_2 = xlwt.easyxf('font: height 150, name Arial, colour_index black, bold off; align: horiz left;'  "borders:  left thin,right thin,bottom thin;")
        date_style = xlwt.easyxf('align: horiz center,wrap yes;' "borders: left thin,right thin,bottom thin,top thin;", num_format_str='DD-MM-YYYY')
        format_3 = xlwt.easyxf('font: height 170, name Arial, colour_index black, bold off; align: horiz center,vert center;'  "borders:  left thin,right thin,bottom thin;")


        
        sheet = book.add_sheet('property offers')
        
        
        sheet.col(0).width = 256 * 5
        sheet.col(1).width = 256 * 4
        sheet.col(2).width = 256 * 8
        sheet.col(3).width = 256 * 4
        sheet.col(4).width = 256 * 4
        
        sheet.col(6).width = 256 * 8
        sheet.col(7).width = 256 * 6
        sheet.col(8).width = 256 * 4
        sheet.col(9).width = 256 * 6
        
        sheet.col(10).width = 256 * 4
        sheet.col(11).width = 256 * 6
        sheet.col(12).width = 256 * 4

        
        
        sheet.write_merge(2,3,0,12,'PROPERTY OFFER LIST',header)
        
        #company details :
        company = self.env.company
        
        print(self.env["res.company"].search_read([('id','=',company.id)],[]))
        
        
        sheet.write_merge(4,4,0,12,company.name,format_1)
        sheet.write_merge(5,5,0,12,company.street,format_1)
        sheet.write_merge(6,6,0,12,f'{company.city},{company.state_id.name},{company.zip}',format_1)
        sheet.write_merge(7,7,0,12,f'Phone: /Email: {company.phone}/{company.email}',format_1)
        
        
        sheet.write_merge(8,8,0,12,'',header)
        sheet.write_merge(9,10,6,12,property.name,format_2)
        
        List = ['Property Name','Salesman','Expected Price','Status']
        row = 9
        for index,value in enumerate(List) :
            sheet.write_merge(row,row + 1,0,5,value,xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz left;'  "borders:  left thin,right thin,bottom thin,top thin;")
)
            row += 2
            

        sheet.write_merge(11,12,6,12,property.sales_person.name,format_2)
        sheet.write_merge(13,14,6,12,property.expected_price,format_2)
        sheet.write_merge(15,16,6,12,property.status,format_2)
        #empty line
#         sheet.write_merge(15,15,0,12,'',header)
        
        row = 17
        if property.offer_ids :
            table_header = ['S.No','Price','Partner','Validity(days)','Deadline','State']
            
            col = 0
            for index,value in enumerate(table_header) :
                if value == 'State' :
                    sheet.write_merge(row,row + 1,col,col+2,table_header[index],header)
                else :
                    sheet.write_merge(row,row + 1,col,col + 1,table_header[index],header)
                    col += 2
            row += 2
            
            offers = self.env["estate.property.offer.fifteen"].search([('property_id','=',id)])
            for index,offer in enumerate(offers) :
                sheet.write_merge(row,row+1,0,1,index + 1,format_3)  
                sheet.write_merge(row,row +1,2,3,offer.price,format_3)
                sheet.write_merge(row, row + 1,4,5,offer.partner_id.name,format_3)
                sheet.write_merge(row,row + 1,6,7,offer.validity,format_3)
                sheet.write_merge(row,row + 1,8,9,offer.dead_line,date_style)
                sheet.write_merge(row,row + 1,10,12,offer.status,format_3)
                
                row += 2
            
           
        else :
            sheet.write_merge(row,row + 1,0,12,'No offers have been made yet',header)

        
        
        
        
        
        
        
        
        
        
        bin =io.BytesIO()
        book.save(bin)
        
        res_id = self.env['excel.report'].create({'excel_file': base64.encodestring(bin.getvalue()),'file_name' : "property offer report.xls" })
            
        sql = f"DELETE from excel_report where id != {res_id.id}"
        
        self.env.cr.execute(sql)
       
        return{
              'view_mode': 'form',
              'res_id': res_id.id,
              'res_model': 'excel.report',
              'type': 'ir.actions.act_window',
              'context': False,
              'target': 'new',
            }
            
        
        
        
        
        
        
        
        
        
        
        
        
    
    