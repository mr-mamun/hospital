# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.1',
    'summary': 'Hospital summary',
    'sequence': 15,
    'description': """
Description for hospital management
    """,
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : [],
    'data': [
        'report/patient_card.xml',
        'report/report.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/patient.xml',
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
