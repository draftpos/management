from odoo import api, fields, models

class ManagementSalesPerformance(models.Model):
    _name = 'management.sales.performance'
    _description = 'Management Sales Performance'

    product_id = fields.Many2one('management.product', string='Product', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    value = fields.Monetary(string='Value', currency_field='currency_id')
    
    sales_rep_id = fields.Many2one('res.users', string='Sales Rep')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
