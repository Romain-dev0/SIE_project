{
    'name': "server status",
    'version': '1.0',
    'depends': ['base'],
    'author': "Devènes Romain",
    'category': 'Category',
    'description': """
    Addons that connect to server API and return a their status.
    """,
    'application': True,
    'data':[
        'views/server_status_views.xml',
        'views/server_status_menus.xml',
        'security/ir.model.access.csv',
    ],
    'external_dependencies': {
    'python': ['requests'],
    }

}