from odoo import api, fields, models

class ManagementClientFollowup(models.Model):
    _name = 'management.client.followup'
    _description = 'Management Client Follow Up'

    customer_id = fields.Many2one('res.partner', string='Customer Name', required=True)
    sales_rep_id = fields.Many2one('res.users', string='Sales Rep')
    technician_id = fields.Many2one('res.users', string='Technician')
    
    date_job_done = fields.Date(string='Date Job Done')
    
    using_system_status = fields.Selection([
        ('not_yet', 'Not Yet'),
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Using System', default='not_yet')
    
    sales_invoices_done_now = fields.Boolean(string='Sales Invoices Done Now')
    scheduled_issues = fields.Text(string='Scheduled Issues')
