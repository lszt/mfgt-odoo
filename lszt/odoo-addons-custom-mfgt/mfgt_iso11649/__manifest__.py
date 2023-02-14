# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT: ISO11649 QR invoice',
    'version': '16.0.0.0',
    'author': 'Motorfluggruppe Thurgau MFGT',
    'website' : 'http://mfgt.ch',
    'category': 'Hidden/Dependency',
    'depends' : [
                'account',
            ],
    'description': """
Automatically create structured reference for QR invoice.
    """,
    'data': [
    ],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {'python' : ['python-stdnum']},
}
