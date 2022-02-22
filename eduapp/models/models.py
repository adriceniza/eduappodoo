# -*- coding: utf-8 -*-

from odoo import models, fields, api





class eduapp_resources(models.Model):
    _name = 'eduapp.resources'
    _description = 'eduapp.resources'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Nombre del recurso')
    description = fields.Char(string='Descripción')
    files = fields.One2many('eduapp.files','eduappFile',string='Files')




class eduapp_files(models.Model):
    _name = 'eduapp.files'
    _description = 'eduapp.files'    
    name= fields.Integer(string='Número de archivo')
    eduappFile = fields.Binary(string='Subir archivo')
    resources = fields.Many2one('eduapp.resources',string='File',ondelete='cascade')

class eduapp_sessions(models.Model):
    _name = 'eduapp.sessions'
    _description = 'eduapp.sessions'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name =fields.Char(string='Session subject')
    date =fields.Date(string='Session date', default= fields.Date.today(), help='Date of the session')
    resourcesPlatform =fields.Char(string='Session resource platform')
    streamingPlatform =fields.Char(string='Session streaming platform')
    user= fields.Many2one('res.partner',string='User',required=True,ondelete='cascade')

    @api.model
    def create(self, values):
        res = super(eduapp_sessions, self).create(values)

        self.env.cr.execute("""SELECT id FROM ir_model WHERE model = %s""", (str(self._name),))

        nuevo1 = self.env['mail.activity'].create({
            'user_id': 2,
            'res_model_id': self.env.cr.dictfetchall()[0]['id'],
            'res_id': res.id,
            'date_deadline': fields.Date.today(),
            'res_name': res.name,
            'note': "<p>SE HA CREADO UNA NUEVA SESIÓN}</p>",
            'summary': "TareaNueva",
            'activity_type_id': 4,
            
        })


        return res


class sessions_clientes(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    sessions = fields.One2many('eduapp.sessions','user',string='Sessions')

