from odoo import models, fields

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    qty_pending = fields.Float(
        string='Cantidad pendiente',
        readonly=True,
        help='Cantidad ordenada menos cantidad recibida'
    )

    def _select_additional_fields(self, fields):
        fields['qty_pending'] = "po_line.product_qty - po_line.qty_received"
        return super()._select_additional_fields(fields)
