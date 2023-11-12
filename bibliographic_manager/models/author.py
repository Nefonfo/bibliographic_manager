from odoo import fields, models


class Author(models.Model):
    _name = 'bibliographic.manager.author'
    _description = 'Reference Author'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)
    name = fields.Char(string='Author Name', required=True)
