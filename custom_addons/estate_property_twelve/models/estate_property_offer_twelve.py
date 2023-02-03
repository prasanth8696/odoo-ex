from datetime import date, timedelta
from odoo import api, models, fields, _
from odoo.exceptions import UserError


class EstatePropertyOfferTwelve(models.Model):
    _name = "estate.property.offer.twelve"
    _description = "offer model for chapter twelve"

    price = fields.Float(string="price")
    creation_date = fields.Date(default = date.today())
    validity = fields.Integer(string="Validity(days)", default=7)
    dead_line = fields.Date(
        string="Dead Line",
        compute="_compute_validity_date",
        inverse="_inverse_validity_date",
    )
    status = fields.Selection(
        string="status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one(
        "estate.property.twelve", string="Property", required=True
    )
    property_type_id = fields.Many2one("property_id.property_type_id" ,string = "property type")
    
    _sql_constraints = [
        ("positive_price","CHECK(price > 0.0)","Offer Price must be positive"),
        ("positive_validity","CHECK(validity >= 0)","Validity must be positive")

                ]
    _order = "price DESC" #for show highest prices on top
    
    @api.depends("validity") 
    def _compute_validity_date(self):
            for record in self :
                record.dead_line = record.creation_date + timedelta(days = record.validity)
             
            
    def _inverse_validity_date(self) :        
        for record in self :
                 record.validity = (record.dead_line - record.creation_date).days #inverse the fieled's dependancies... 
             

            
    def accept_offer(self):
        property = self.property_id

        # check property is canceled or not
        if property.status == "canceled":
            raise UserError(_("it is a Canceled property"))

        accept_list = property.offer_ids.mapped("status")

        # check already offer is accepted or not
        # if any one of the offer is accepted throw user error
        if accept_list.count("accepted") > 0:
            raise UserError(_("you already accepted one offer previously"))

        else:
            property.buyer = self.partner_id
            property.selling_price = self.price
            property.status = "offer accepted"
            self.status = "accepted"

    def refuse_offer(self):
        property = self.property_id

        # check property is canceled or not
        if property.status == "canceled":
            raise UserError(_("it is the canceled property"))

        # check offer is accepted or not

        if self.status == "accepted" :
            raise UserError(_("you cannot revoke offer once offer is accepted"))

        # case 1: offer not yet accepted(here you can use one else condition for both cases)
        else:
            self.status = "refused"
