from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StudyGroup(models.Model):
    _name = 'bibliographic.manager.study.group'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Group that relation the folders and users'

    name = fields.Char(string="Group Name", required=True, tracking=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id, string='Owner', tracking=True)
    member_ids = fields.Many2many('res.users', 'study_group_user_rel', string="Members", tracking=True)
    folder_ids = fields.Many2many('bibliographic.manager.folder', 'study_group_folders_rel', string="Related Folders", tracking=True)

    @api.constrains('name')
    def _check_name(self):
        for folder in self:
            if self.env['bibliographic.manager.study.group'].search_count(
                    ['&', ('name', '=', folder.name), ('user_id', '=', folder.user_id.id)]) > 1:
                raise ValidationError('Folder Name Already Exists')
