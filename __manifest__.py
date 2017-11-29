# -*- coding: utf-8 -*-
{
    'name': "Drag & Drop",

    'summary': """
        Attachment Drag and Drop""",

    'description': """
        With this module you are able to:
         * Drag your files to the form-view and add it to the attachments
         * Add Screenshots to the form-view (Attachment, Message or internal Message)
    """,

    'author': "Cytex",
    'website': "http://www.cytex.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'document', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}