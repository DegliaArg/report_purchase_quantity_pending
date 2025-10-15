from odoo import models, fields, api

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    difference_quantity = fields.Float(
        string='Cantidad Pendiente',
        readonly=True,
        help='Diferencia entre la cantidad ordenada y la cantidad recibida.',
        compute='_compute_difference_quantity',
        store=False,
        group_operator='sum',
    )

    @api.depends('qty_ordered', 'qty_received')
    def _compute_difference_quantity(self):
        for record in self:
            record.difference_quantity = record.qty_ordered - record.qty_received
