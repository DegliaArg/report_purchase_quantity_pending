from odoo import models, fields, api

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    difference_quantity = fields.Float(
        string='Cantidad pendiente',
        readonly=True,
        help='Diferencia entre la cantidad ordenada y la cantidad recibida.',
        compute='_compute_difference_quantity',
        store=False,
        group_operator='sum',
    )

    # NUEVO: Precio unitario = Total / Cantidad ordenada
    unit_price = fields.Float(
        string='Precio unitario',
        readonly=True,
        help='Total / Cantidad ordenada',
        compute='_compute_unit_price',
        store=False,
        group_operator='avg',  # promedio simple en agrupaciones
        digits='Product Price',
    )

    @api.depends('qty_ordered', 'qty_received')
    def _compute_difference_quantity(self):
        for record in self:
            record.difference_quantity = record.qty_ordered - record.qty_received

    @api.depends('qty_ordered')  # total se obtiene vía getattr, evita fallos si el nombre difiere
    def _compute_unit_price(self):
        for record in self:
            # Usa price_total si existe; si no, intenta amount_total; si no, 0.0
            total = getattr(record, 'price_total', None)
            if total is None:
                total = getattr(record, 'amount_total', 0.0)

            qty = record.qty_ordered or 0.0
            record.unit_price = (total / qty) if qty else 0.0
