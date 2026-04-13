# -*- coding: utf-8 -*-

{
    'name': 'Report DOCX generted',
    'description': 'Is Easy an elegant and scalable solution to design reports'
                   'using Microsoft Office.',
    'summary': 'Export data all objects odoo to Microsoft Office output'
                   ' files docx, pdf',
    'category': 'All',
    'version': '17.0.1.0.0',
    'website': 'https://github.com/LeapAI-SA',
    "license": "LGPL-3",
    'author': 'Abdulkrim Osman',
    'depends': [
        'base', 'web'
    ],
    "external_dependencies": {
        "bin": ["unoconv"],
    },
    'data': [
        'data/templates.xml',
        'report.xml',
        'views/report_view.xml'
    ],
    'live_test_url': 'https://youtu.be/919YFe4mtkc',
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'leapai_magre/static/src/scss/theme_screenshot.scss',
        ]
    }
}
