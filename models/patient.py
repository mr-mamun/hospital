from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):

    _name = 'hospital.patient'
    #_inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Records'
    _rec_name = 'patient_name'
    _order = 'patient_age desc'

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('the age must be greater than 4'))

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    def _get_default_note(self):
        return "this is a sample default note"

    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    # class ResPartners(models.Model):
    #     _inherit = 'res.partner'
    #
    # @api.model
    # def create(self, vals_list):
    #     res = super(ResPartners, self).create(vals_list)
    #     print("Its working")
    #     return res

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string='Gender',
        required=True,
        default='male')
    age_group = fields.Selection(
        [('major', 'Major'), ('minor', 'Minor')],
        string='Age Group', compute='set_age_group')
    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes', default=_get_default_note)
    doctor_note = fields.Text(string='Doctors Notes')
    pharmacy_note = fields.Text(string='Pharmacys Notes')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                        index=True, default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result