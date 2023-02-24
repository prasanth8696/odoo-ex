from odoo import fields,models


class ExcelReport(models.Model):
    _name = "excel.report"
    
    _description = "for excel report"
    
    name=fields.Char(string="Name",default='Download Excel Report')
    excel_file = fields.Binary('Download report Excel')
    file_name = fields.Char('File Name', size=64) 