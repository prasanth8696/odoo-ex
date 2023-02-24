from odoo import http


class RealEstate(http.Controller):
    
    
    @http.route('/estate', auth='public' ,website=True)
    def index(self, **kw):
        Properties = http.request.env["estate.property.fifteen"]
        return http.request.render('estate_property_fifteen.index', {
             'properties': Properties.search([])
             }
            )
#         
    @http.route('/estate/getProperty' ,auth='public',website=True)
    def get_property_by_name(self,**kwargs):
        try :
            property_name = kwargs["name"]
            property = http.request.env["estate.property.fifteen"].search([('name','=',property_name)])
            return http.request.render('estate_property_fifteen.index', {
             'properties': property})
        except KeyError:
            http.request.not_found(description = "item not found")
        
         
        
#         property = http.request.env["estate.property.fifteen"].browse(name)
#          
#         return http.request.render(
#             "estate_property_fifteen.index",{"property" : property})