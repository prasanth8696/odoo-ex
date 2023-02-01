from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import api, models, fields, _
from odoo.exceptions import UserError


# estate property model
class EstatePropertyTen(models.Model):
    _name = "estate.property.ten"
    _description = "estate property model ten"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    post_code = fields.Char(string="PostCode")
    date_availability = fields.Date(
        string="Available From",
        copy=False,
        default=date.today() + relativedelta(months=3),
    )  # add default value
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(
        string="Selling Price", readonly=True, copy=False
    )  # copy = false >>> prevent dublicate value
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string="GardenOrientation",
        selection=[
            ("east", "East"),
            ("west", "West"),
            ("north", "North"),
            ("south", "South"),
        ],
    )  # (value,label)
    status = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer received", "Offer Received"),
            ("offer accepted", "Offer Accepted"),
            ("canceled", "Canceled"),
            ("sold", "Sold"),
        ],
        default="new",
        store=True,
    )
    active = fields.Boolean("active", default=True)
    property_type_id = fields.Many2one(
        "estate.property.type.ten", string="Property Type", required=True
    )
    sales_person = fields.Many2one(
        "res.users", string="Sales person", default=lambda self: self.env.user
    )
    buyer = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag.ten", string="tags")
    offer_ids = fields.One2many(
        "estate.property.offer.ten", "property_id", string="Offer"
    )
    total_area = fields.Integer(compute="_compute_total", string="Total Area")
    best_offer = fields.Float(compute="_compute_best_price", string="Best Offer")

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            prices = record.offer_ids.mapped("price")
            record.best_offer = max(prices) if prices != [] else 0.0

    @api.onchange("garden")
    def _onchange_garden_crends(self):

        if self.garden:  # if garden is Available(value is True)
            self.garden_area = 10
            self.garden_orientation = "north"
        else:  # if garden  is unavailable (value is False)
            self.garden_area = 0
            self.garden_orientation = None

    # for sold the property
    def sold_property(self):
        # check the property is cancel or not
        # if state is cancel throw userError
        if self.status == "canceled":
            raise UserError(_("canceled property cannot be sold"))
        else:
            self.status = "sold"

    def cancel_property(self):
        # check property status is offer accepted if yes means raise user error
        if self.status == "offer accepted":
            raise UserError(_("you cannot cancel offer accepted property"))
        # check the property is sold or not
        # if state is offer accepted throw userError
        if self.status == "sold":
            raise UserError(_(" sold property cannot be canceled."))
        else:
            self.status = "canceled"
