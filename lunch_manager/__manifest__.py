{
    'name': "Lunch Manager",
    'version': '1.1',
    'category': 'Extra tools',
    'depends': ['base', 'mail', 'uom'],
    'description': """
            Long description of module's purpose
        """,

    'data': [
        'security/ir.model.access.csv',
        'views/lunch.xml',
    ],

    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}