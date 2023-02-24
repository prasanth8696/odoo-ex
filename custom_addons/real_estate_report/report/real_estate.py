# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from pygments.lexer import _inherit


class RealEstate(models.Model):
    _inherit = 'real.estate.report.wzd'
   
    def print_real_estate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'start_date':self.start_date if self.start_date else False,
                'end_date':self.end_date if self.end_date else False,
                'company_id':self.company_id if self.company_id else False,
            },
        }

        return self.env.ref('real_estate_report.real_estate_details_report').report_action(self, data=data, config=False)
