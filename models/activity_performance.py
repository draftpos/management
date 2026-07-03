from odoo import api, fields, models

class ManagementActivityType(models.Model):
    _name = 'management.activity.type'
    _description = 'Management Activity Type'

    name = fields.Char(string='Name', required=True)
    code = fields.Selection([
        ('cold_calls', 'Cold Calls'),
        ('calls_done', 'Calls Done'),
        ('door_to_door', 'Door to Door'),
        ('other', 'Other')
    ], string='Type Code', default='other')

class ManagementActivityPerformance(models.Model):
    _name = 'management.activity.performance'
    _description = 'Management Activity Performance'

    activity_type_id = fields.Many2one('management.activity.type', string='Activity Type', required=True)
    activity_type_code = fields.Selection(related='activity_type_id.code', string='Type Code', store=False)
    
    qty_done = fields.Integer(string='Qty Done')
    expected_qty = fields.Integer(string='Expected Qty')
    product_id = fields.Many2one('management.product', string='Product')
    
    leads_generated = fields.Integer(string='Leads Generated')
    unanswered_calls = fields.Integer(string='Unanswered Calls')
    leads_done = fields.Integer(string='Leads Done')
