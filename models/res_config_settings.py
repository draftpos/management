from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    management_default_expected_leads = fields.Integer(
        string='Default Expected Leads',
        config_parameter='management_app.default_expected_leads',
        default=10,
        help="Set the default expected leads for new marketing campaigns."
    )
