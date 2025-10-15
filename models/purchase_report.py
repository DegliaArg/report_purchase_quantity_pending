from odoo import models, fields
from odoo.tools.sql import SQL

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    qty_pending = fields.Float(
        string='Cantidad pendiente',
        readonly=True,
        help='Cantidad ordenada menos cantidad recibida',
    )

    def _select(self):
        sql = super()._select()
        sql.add(SQL(", (SUM(l.product_qty) - SUM(l.qty_received)) AS qty_pending"))
        return sql
