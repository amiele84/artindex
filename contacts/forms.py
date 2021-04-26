
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset, Row, Column


from django import forms 
from .models import *



class NewContactUploadForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        
        ##birth_date & death_date don't work##
        fields = [
            'first_name', 'middle_name', 'last_name',
            'job_title', 'company', 'email', 'phone_number',
            'bio', 'notes','contact_types', 'contact_image',
            'birth_date', 'death_date',
            ]
        
    ##form helper
    ##adapted from: https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
    def __init__(self, *args, **kwargs):
        super(NewContactUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id_new_upload_form'
        self.helper.form_class = 'uploadForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'upload_piece'
        self.helper.layout = Layout(
            Fieldset('contact_image',
                    Field('piece_upload', placeholder='Drag/Drop pieces here'),
            ),
            Fieldset(
            'first_name', 'middle_name', 'last_name',
            'job_title', 'company', 'email', 'phone_number',
            'bio', 'notes','contact_types',
            'birth_date', 'death_date',
            )
        ),
        Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('middle_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        Row(
                Column('job_title', css_class='form-group'),
                Column('company', css_class='form-group col-sm-2 mb-0'),
                css_class='form-row'
            ),

        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean_uploader(self):
        if not self.cleaned_data['uploader']:
            return User()
        return self.cleaned_data['uploader']
