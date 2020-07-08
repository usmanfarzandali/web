# -*- coding: utf-8 -*-

{
    'name': 'PDF Viewer',
    'summary': 'PDF Viewer Widget.',
    'version': '12.0.1.0.0',
    'author': 'Nebil Aydi',
    'website': 'https://github.com/aydi-nebil/web/tree/11.0/web_tree_no_open',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'web'],
    'data': [
        'views/assets.xml',
    ],
    'qweb': ['static/src/xml/pdf_viewer.xml'],
}
