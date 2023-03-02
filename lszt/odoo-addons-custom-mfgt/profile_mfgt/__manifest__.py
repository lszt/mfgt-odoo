# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Profile MFGT - Motorfluggruppe Thurgau (disabled)',
    'version': '16.0.0.1.0',
    'author': 'Motorfluggruppe Thurgau MFGT',
    'category': 'Custom',
    'website': 'https://www.mfgt.ch/',
    'licence': 'AGPL-3',
    'summary': 'Customizations for MFGT',
    'depends': [
        'account_payment_order',
    ],
    'data': [
       'report/reports.xml',
#       'report/layouts.xml',
#       'report/report_saleorder.xml',
#       'report/report_purchasequotation.xml',
#       'report/report_purchaseorder.xml',
#       'report/report_invoice.xml',
#       'data/report_paperformat.xml',
#       'data/account_tags.xml',
#       'report/product_label.xml',
#       'views/account_move_view.xml',
#       'views/sale_order.xml',
#       'views/stock.xml',
#       'report/report_deliveryslip.xml',
    ],
    'installable': True,
    'application': False,
}
