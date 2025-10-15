from odoo import models, fields

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    qty_pending = fields.Float(
        string='Cantidad pendiente',
        readonly=True,
        help='Cantidad ordenada menos cantidad recibida',
    )

    def _select(self):
        # extendemos el SELECT SQL original
        return super()._select() + ", (SUM(l.product_qty) - SUM(l.qty_received)) AS qty_pending"

    def _group_by(self):
        # mantenemos el group_by igual al original
        return super()._group_by()
