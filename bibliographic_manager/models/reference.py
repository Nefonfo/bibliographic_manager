from odoo import fields, models


class Reference(models.Model):
    _name = 'bibliographic.manager.reference'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Bibliographic Reference'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, tracking=True)
    folder_ids = fields.One2many('bibliographic.manager.folder', 'references_ids', string='Folders')
    # Standard fields for reference
    type = fields.Selection(
        selection=[
            ('website', 'Website'),
            ('book', 'Book'),
            ('more', 'More')
        ],
        required=True,
        default='website',
        tracking=True
    )
    format = fields.Selection(
        selection=[
            ('apa', 'Apa'),
            ('chicago', 'Chicago'),
            ('mla', 'MLA'),
            ('iee', 'IEE')
        ],
        required=True,
        default='apa',
        tracking=True
    )
    name = fields.Char(string='Title', required=True, tracking=True)
    author_ids = fields.Many2many('bibliographic.manager.author', 'reference_author_rel', string='Author', tracking=True)
    publish_date = fields.Date(string='Publish Date', tracking=True)
    # Fields for website references
    page_name = fields.Char(string='Page Name', tracking=True)
    source_access_date = fields.Date(string='Access Date', tracking=True)
    url = fields.Char(string="URL", tracking=True)
    # Fields for Books
    location = fields.Char(string='Location', tracking=True)
    publishing_house = fields.Char(string='Publish House', tracking=True)
    book_volume = fields.Char(string='Book Volume', tracking=True)
    book_edition = fields.Char(string='Book Edition', tracking=True)
    book_page = fields.Char(string='Book Page', tracking=True)
    book_file = fields.Binary(string='Book File', tracking=True)
    # Fields for Others
    type_of_publication = fields.Selection(
        selection=[
            ('newspaper', 'Newspaper'),
            ('movies', 'Movies'),
            ('others', 'Others')
        ],
        tracking=True
    )
    other_location = fields.Char(string='Other Location', tracking=True)
    is_online_source = fields.Boolean(default=True, string="Online Resource", tracking=True)

    def action_show_reference(self):
        self.ensure_one()
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'bibliographic.manager.reference',
            'context': self.env.context,
            'target': 'current',
            'res_id': self.id
        }
