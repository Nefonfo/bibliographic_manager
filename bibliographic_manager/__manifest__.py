{
    "name": "Bibliographic Manager",
    "summary": "Module to manage Bibliographic References",
    "description":
    """
        Module to manage Bibliographic References
    """,
    "category": "Bibliographic",
    "version": "0.0.1",
    "author": "Sycorax Corp.",
    "website": "https://www.odoo.com/",
    "license": "GPL-3",
    "depends": [
        "mail"
    ],
    "data": [
        #"security/bibliographic_manager_security.xml",
        "security/ir.model.access.csv",
        "views/reference_views.xml",
        "views/folder_views.xml",
        "views/study_group_views.xml",
        "views/bibliographic_manager_menus.xml",
    ],
    "application": True
}
