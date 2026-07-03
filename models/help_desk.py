from odoo import api, fields, models

class ManagementHelpDesk(models.Model):
    _name = 'management.helpdesk'
    _description = 'Management Help Desk'

    name = fields.Char(string='Ticket Reference', required=True, copy=False, readonly=True, default=lambda self: 'New')
    customer_id = fields.Many2one('res.partner', string='Customer Name', required=True)
    phone = fields.Char(related='customer_id.phone', string='Phone', readonly=False)
    
    sales_rep_id = fields.Many2one('res.users', string='Sales Rep')
    issue_type = fields.Char(string='Issue Type')
    product_id = fields.Many2one('management.product', string='Product')
    technician_id = fields.Many2one('res.users', string='Assigned Tech')
    
    time_to_be_taken = fields.Float(string='Time to be Taken (Hours)')
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    time_taken_to_resolve = fields.Float(string='Time Taken to Resolve (Hours)', compute='_compute_time_taken', store=True)
    
    status = fields.Selection([
        ('not_assigned', 'Not Assigned'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('overdue', 'Overdue')
    ], string='Status', default='not_assigned')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('management.helpdesk') or 'New'
        return super().create(vals_list)

    @api.depends('start_time', 'end_time')
    def _compute_time_taken(self):
        for record in self:
            if record.start_time and record.end_time:
                delta = record.end_time - record.start_time
                record.time_taken_to_resolve = delta.total_seconds() / 3600.0
            else:
                record.time_taken_to_resolve = 0.0
