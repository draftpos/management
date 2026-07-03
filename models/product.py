from odoo import api, fields, models

class ManagementProduct(models.Model):
    _name = 'management.product'
    _description = 'Management Product'

    item_code = fields.Char(string='Item Code', required=True, copy=False, readonly=True, default=lambda self: 'New')
    name = fields.Char(string='Name', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('item_code', 'New') == 'New':
                vals['item_code'] = self.env['ir.sequence'].next_by_code('management.product') or 'New'
        return super().create(vals_list)

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.item_code}] {record.name}"
            result.append((record.id, name))
        return result
