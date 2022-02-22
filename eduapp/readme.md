<h1>EDUAPP CRUD PANEL IN ODOO</h1>


    1-Nuevas clases base del nuevo módulo. (1 punto)
        En models/models.py
    2-Nuevas vistas base del nuevo módulo. (1 punto)
        En views/views.xml
    3-Clases heredadas de otras clases existentes en otros módulos propios de Odoo. (1 punto)
        En models/models.py
            Tanto en el modulo de resources como en el de sessions , _inherit attribute.
    4-Vistas heredadas de otras vistas existentes en otros módulos propios de Odoo.
     Se debe apreciar modificaciones en las vistas de esos otros módulos. (1 punto)
        En views/views.xml 
            En la vista de sessions
                Este es el codigo
```bash
    <record id="res_partner_view_form_inherit_sessions" model="ir.ui.view">
        <field name="name">res.partner.view.form.inherit.eduapp</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml">
            <xpath expr="//page[@name='internal_notes']" position="after">
            <page string="Eduapp" name="Ficha_eduapp_users">
                <field name="sessions">
                <tree>
                    <field name="name"/>
                    <field name='date'/>
                    <field name='resourcesPlatform'/>
                    <field name='streamingPlatform'/>
                </tree>
                </field>
            </page>
            </xpath>
        </field>
    </record>
```
    5-Acciones, Elementos de menú y Grupos de permisos. (1 punto)
        En views/views.xml
    6-Inclusión de campos del tipo one2many y many2one. (1 punto)
        En models.py
    7-Adaptación a nuestro módulo de alguna funcionalidad implementada en algún módulo base de Odoo. (1 punto)
        En el modelo y en la vista de sessions.
    8-Creación de flujos de trabajo. (2 puntos)
        En el modulo de sessions , en models.
    9-Aportaciones personales al módulo creado. (1 punto)