# -*- coding: utf-8 -*-

{
    'name': "Generic defaults",
    'version': '14.0.1.0.0',
    'summary': """
        Establece varios parámetros default automáticamente
    """,
    'description': """
    """,
    'category': 'Uncategorized',
    'author': "",
    'website': "",
    'depends': [
# addons ODOO
        'account',
        'base',
        'calendar',
        'contacts',
        'crm',
        'google_drive',
        'hr',
        'mrp',
        'note',
        'purchase',
        'sale_management',
        'sales_team',
        'stock_account',
        'stock',
# addons 3rd party
        'backend_theme_v14',
#        'base_territory',
        'base_user_show_email',
        'company_country',
        'disable_odoo_online',
##        'fieldservice_account',
##        'fieldservice_activity',
##        'fieldservice_recurring',
##        'fieldservice_timeline',
#        'fieldservice',
        'hide_powered_by_and_manage_db',
#        'login_user_detail',
        'mail_outbound_static',
        'remove_odoo_enterprise',
        'report_xlsx',
        'rowno_in_tree',
        'web_environment_ribbon',
        'web_responsive',
        'web_timeline',
# addons NUMA básicos
        'numa_exceptions',
#        'numa_pricelist',
#        'numa_background_job',
#        'numa_payment',
        # Contabilidad para ODOO Community
        'base_accounting_kit', # Cybrosys Full Accounting Kit
        'dynamic_accounts_report', # Cybrosysy Dynamic Financial Reports
#        'numa_physical_product',
#        'numa_account_community',
        # Sin dependencias
#        'numa_address_extended', # ???
#        'numa_periodic_services',
#        'numa_product_multi_category',
#        'numa_product_variant',
#        'numa_synch',
    ],
    'data': [
        'data/01-set-defaults.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}