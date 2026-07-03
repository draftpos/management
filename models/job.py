from odoo import api, fields, models

class ManagementJob(models.Model):
    _name = 'management.job'
    _description = 'Management Job'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Job Name', required=True, tracking=True)
    sales_rep_ids = fields.Many2many('res.users', 'job_sales_rep_rel', string='Sales Rep')
    technician_ids = fields.Many2many('res.users', 'job_technician_rel', string='Technician')
    
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    amount_quoted = fields.Monetary(string='Amount Invoiced', currency_field='currency_id', tracking=True)
    
    organization_id = fields.Many2one('res.partner', string='Organization Name', tracking=True)
    next_contact_date = fields.Date(string='Next Contact Date', tracking=True)
    product_id = fields.Many2one('management.product', string='Product', tracking=True)
    
    address_line = fields.Char(string='Address Line')
    city = fields.Char(string='City/Town')
    country_id = fields.Many2one('res.country', string='Country', default=lambda self: self.env['res.country'].search([('name', '=', 'Zimbabwe')], limit=1))
    
    status = fields.Selection([
        ('to_be_done', 'To Be Done'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('demo_scheduled', 'Demo Scheduled')
    ], string='Status', default='to_be_done', tracking=True)
