from datetime import date, timedelta
from odoo import api, models, fields, _
from odoo.exceptions import UserError


class EstatePropertyOfferTen(models.Model):
    _name = "estate.property.offer.ten"
    _description = "offer model for chapter ten"

    price = fields.Float(string="price")
    create_date = fields.Date(default=date.today())
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
        "estate.property.ten", string="Property", required=True
    )

    @api.depends("validity")
    def _compute_validity_date(self):

        for record in self:
            record.dead_line = record.create_date + timedelta(days=record.validity)

    @api.depends("dead_line")
    def _inverse_validity_date(self):
        for record in self:
            if record.dead_line:
                record.validity = (
                    record.dead_line - record.create_date
                ).days  # inverse the filed's dependancies...

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
            raise UserError(_("you already accepted one offer previously"))

        # check offer is accepted as well as property is sold if property is sold you cannot revoke the offer

        if self.status == "accepted" and property.status == "sold":
            raise UserError(_("you cannot revoke the offer after property is sold"))
        # else 2 cases
        # case 1 : offer is accepted only but not sold
        # case 2 : offer not yet accepted(here you can use one else condition for both cases)
        else:
            property.buyer = None
            property.selling_price = 0.0
            property.status = "offer received"
            self.status = "refused"
