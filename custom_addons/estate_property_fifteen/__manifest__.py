{
    'name' : 'real estate fifteen',
    'version' : '1.0',
    'depends' : ['base','website','sale'],
    'author' : 'ayyappan',
    'category' : 'Real Estate/Brokerage',
    'description' : '''
    this is my first module ''',
    
    'data' : ["wizard/cancel_wizard.xml",
              "wizard/print_property_report_wzd.xml",
              'views/estate_property_tag_fifteen_views.xml',
              'views/estate_property_fifteen_views.xml',
              'views/estate_property_type_fifteen_views.xml',
              'views/estate_property_fifteen_menu.xml',
              'security/ir.model.access.csv',
              'security/security.xml',
              'views/estate_property_offer_fifteen_views.xml',
              "reports/report.xml",
               "data/templates.xml"
              ],
    
    'application': True
    
    }


