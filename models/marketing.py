from odoo import api, fields, models

class ManagementMarketing(models.Model):
    _name = 'management.marketing'
    _description = 'Management Marketing'

    name = fields.Char(string='Ad Name', required=True)
    sales_rep_id = fields.Many2one('res.users', string='Sales Rep')
    product_id = fields.Many2one('management.product', string='Product')
    campaign = fields.Char(string='Campaign')
    
    def _default_expected_leads(self):
        return int(self.env['ir.config_parameter'].sudo().get_param('management_app.default_expected_leads', default=10))

    expected_leads = fields.Integer(string='Expected Leads', default=_default_expected_leads)
    actual_leads = fields.Integer(string='Actual')
    lost_leads = fields.Integer(string='Lost')
    
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    cost_per_lead = fields.Monetary(string='Cost per Lead', currency_field='currency_id')
    
    date = fields.Date(string='Date', default=fields.Date.context_today)
    day_of_week = fields.Selection([
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday')
    ], string='Day of the Week', compute='_compute_day_of_week', store=True)

    @api.depends('date')
    def _compute_day_of_week(self):
        for record in self:
            if record.date:
                record.day_of_week = str(record.date.weekday())
            else:
                record.day_of_week = False
