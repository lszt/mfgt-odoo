# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT Vendor Invoice Reference Warning (dummy)',
    'version': '16.0.1.0',
    'author': 'Motorfluggruppe Thurgau MFGT',
    'website' : 'https://mfgt.ch',
    'category': 'Accounting',
    'description': """
Changes raise user error to only give warning if a vendor reference is duplicated in Odoo.
    """,
    'depends' : [
        'account',
    ],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}
