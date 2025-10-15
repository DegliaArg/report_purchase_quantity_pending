from odoo import models, fields

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    qty_pending = fields.Float(
        string='Cantidad pendiente',
        readonly=True,
        help='Cantidad ordenada menos cantidad recibida'
    )

    def _select_additional_fields(self, fields):
        res = super()._select_additional_fields(fields)
        res['qty_pending'] = "(SUM(l.product_qty) - SUM(l.qty_received))"
        return res
