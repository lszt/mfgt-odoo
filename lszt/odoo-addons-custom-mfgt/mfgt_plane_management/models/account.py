# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_id = fields.Many2one('sale.order', compute='_select_sale_order', string='Sale Order', store=True)
    plane_id = fields.Many2one('mfgt.plane.management', string='Plane', readonly=True, states={'draft': [('readonly', False)]})

    @api.depends('invoice_origin')
    def _select_sale_order(self):
        for rec in self:
            if rec.invoice_origin:
                sale_order = self.env['sale.order'].search([('name', '=', rec.invoice_origin)])
                if sale_order:
                    rec.sale_id = sale_order[0].id
