# -*- coding: utf-8 -*-
{
    'name': 'Real Estate Report',
    'version': '1.0',
    'author': "TenthPlanet",
    'website': "http://tenthplanet.in",
    'summary': '',
    'description': """
        
""",
    'depends': ['base'],
    'data': [   
        'views/real_estate_excel_report_views.xml',
        'views/real_estate_pdf_report.xml',
        'security/ir.model.access.csv',
  
     ],
#    'assets': {
#         'web.assets_backend': [
#             'fc_pos_reports/static/src/js/action_manager.js',
#             'fc_pos_reports/static/src/js/pos_report.js',
#             'fc_pos_reports/static/src/css/pos_report.css'
#         ],
#         'web.assets_qweb': [
#             'fc_pos_reports/static/src/xml/pos_report_view.xml',
#             
#         ],
#     }, 
    'installable': True,
    'auto_install': False,
}
