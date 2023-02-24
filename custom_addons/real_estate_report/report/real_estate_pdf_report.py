# -*- coding: utf-8 -*-
 
from datetime import datetime, timedelta
 
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

 
class RealEstateDetailsReport(models.AbstractModel):    
    _name = 'report.real_estate_report.realestate'
 
    #@api.model
    def _get_report_values(self, docids, data=None):
        start_date = data['form']['start_date']
        end_date = data['form']['end_date']
        company_id = data['form']['company_id']

        
        sql = '''       
            select property_name,property_type,buyer,seller,selling_price,date as date from real_estate_line 
            where real_estate_id=(select max(real_estate_id) from real_estate_line)   
             '''
#         if start_date and end_date:
#                 sql += "and pos.date_order between '%s' and '%s'" % (start_date, end_date)
        self.env.cr.execute(sql)
        #print('PDF Report-->',sql)  
        count_data = self.env.cr.dictfetchall()
        docs = []
        seq = 0
        for line in count_data:
            #print('PDF line--->',line)
            seq += 1
            today = fields.Date.today()
            todaydate = fields.Date.from_string(today)
            #invoicedate=fields.Date.from_string(inv_date)
            #null =''
            daysdue = ''
#             if invoicedate :
#                 daysdue = ((todaydate) - (invoicedate)).days
#                 
#             bill_no = line['bill_no']
#             partner_id = line['alias_name']
#             partner_id = line['partner_id']
#             if bill_no is None:
#                 line['alias_name'] = null
#             if bill_no is None:
#                 line['partner_id'] = null
#             if line['pending_days'] == 0:
#                 continue
            docs.append({
                                
                                'property_name' : line['property_name'],
                                'property_type' : line['property_type'],
                                'buyer' :line['buyer'], 
                                'seller' : line['seller'],
                                'selling_price' : line['selling_price'],
                                'date':line['date'],
            })
                       
        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'start_date':start_date,
            'end_date':end_date, 
            'company_id':company_id,
            'docs':docs,
            }
        
        

        
        
