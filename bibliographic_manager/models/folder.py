from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Folder(models.Model):
    _name = 'bibliographic.manager.folder'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Folder For References'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)
    name = fields.Char(string='Folder Name', required=True, tracking=True)
    references_ids = fields.Many2many('bibliographic.manager.reference', 'folder_reference_rel', string='References', tracking=True)
    study_group_ids = fields.One2many('bibliographic.manager.study.group', 'folder_ids', string='Related Groups')

    @api.constrains('name')
    def _check_name(self):
        for folder in self:
            if self.env['bibliographic.manager.folder'].search_count(['&', ('name', '=', folder.name), ('user_id', '=', folder.user_id.id)]) > 1:
                raise ValidationError('Folder Name Already Exists')
