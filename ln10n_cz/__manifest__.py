{
    'name' : 'Czech Republic - Accounting',
    'version' : '1.0',
    'category': 'Localization',
    'description': """
This is the module to manage the accounting chart for Czech Republic in Odoo.
==================================================================================
    """,
    'author': 'Amevia s.r.o.',
    'price': '0',
    'currency': '',
    'website': 'https://amevia.eu/sluzby',
    'depends' : [
        'account',
    ],
    'data': [
        'data/account_group.xml',
        'data/account_account_tag.xml',
        'data/l10n_cz_chart_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_data.xml',
    ],
}
