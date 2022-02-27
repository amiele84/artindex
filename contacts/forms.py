
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset, Row, Column, HTML


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



                        ### test ###

##1/9/22
from .models import *
class ContactImageForm(forms.ModelForm):
    class Meta:
        model = ContactImage
        fields = ('image',)


##1/18/22
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('city', 'state', 'zip_code')







from django.urls import reverse_lazy #1
from django.forms import Textarea, CharField

class UploadContactForm(forms.ModelForm):

    class Meta:
        model = Contact_test
        fields = [
            'first_name', 'middle_name', 'last_name',
            'job_title', 'company', 'city', 'state', 'zip_code', 
            'email', 'phone_number',
            'bio', 'notes','contact_types', 'contact_image',
            'birth_day', 'birth_month', 'birth_year',
            'death_day', 'death_month', 'death_year',
            ]
        
        widgets = {
            'bio': Textarea(attrs={'cols': 100, 'rows': 4, 'style': 'border-color:#609dec; border-radius: 10px; color: #afb1b4;'}), #01-13
            'notes': Textarea(attrs={'cols': 100, 'rows': 4, 'style': 'border-color:#609dec; border-radius: 10px; color: #afb1b4'}), #01-13
        }
    #tags
    #use "MultiValueField"

    ##form helper
    ##adapted from: https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
    def __init__(self, *args, **kwargs):
        super(UploadContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id_new_upload_form'
        self.helper.form_class = 'uploadForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'uploadcontact' #where submit redirects to
        self.helper.form_show_labels = False #hides all labels
        self.helper.form_style='inline'
        self.helper.layout = Layout(
        Div(
            
            Div(
                    Div(Column('first_name'), css_class='form-group first-name-class'),
                    Div(Column('middle_name'), css_class='form-group middle-name-class'),
                    Div(Column('last_name'), css_class='form-group last-name-class'),
                css_class='form-row'),
            css_class='box-1'),


            Div(
                Row(
                    Div(Column('job_title'), css_class='form-group job-class'),
                    Div(Column('company'), css_class='form-group company-class'),
                css_class='form-row'),

                Row(
                    Div(HTML("<p><strong>+ Add Address"), css_class = 'add-address-row')),

            css_class='box-2'),


            Div(
                Div("city", css_class='form-group col-md-2 city-class'),
                Div("state", css_class='form-group col-md-2 state-class'),
                Div('zip_code', css_class='form-group col-md-2 zip-class'),
            css_class='form-row box-3', id="theDIV"),


            Div(
                Row(
                    Row(
                        Div(HTML('<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16"><path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"/></svg>'), css_class='envelope-class'),
                        Field("contact_types", css_class='form-group col-md-12 mb-0 types-class'),
                        Div(Field("email"), css_class='form-group contact-class'),
                        css_class="form-row"),
                css_class='form-row'),

                Row(
                    HTML("<p><strong>+ Add Email"), 
                    css_class = 'add-frame-row'),

            css_class='box-4'),


            Div(
                Row(
                    Row(
                        Div(HTML('<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 16"><path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/></svg>'), css_class='envelope-class'),
                        Field("contact_types", css_class='form-group col-md-12 mb-0 types-class'),
                        Div(Field("phone_number"), css_class='form-group contact-class'),
                        css_class="form-row"),
                css_class='form-row'),

                Row(
                    HTML("<p><strong>+ Add Phone Number"), 
                    css_class = 'add-frame-row'),
                    
            css_class='box-5'),


            Div(
                Row(
                    Row(
                        Div(HTML('<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 16"><path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/></svg>'), css_class='envelope-class'),
                        Field("contact_types", css_class='form-group col-md-12 mb-0 types-class'),
                        Div(Field("phone_number"), css_class='form-group contact-class'),
                        css_class="form-row"),
                css_class='form-row'),


                Row(
                    HTML("<p><strong>+ Add Phone-number"), 
                    css_class = 'add-frame-row'),
                    
            css_class='box-6'),


            Div(
                Row(
                    Column(
                        
                        Div(
                            Div(HTML("<p><strong>Birthday"), css_class='birth-label'),
                            Div(HTML("<p><strong>Death Date"), css_class='death-label'),
                            css_class='form-row dates-labels'),
                        
                        Row(
                            Div(
                                Row(
                                    Div('birth_month', css_class = 'birth-month-class'),
                                    Div('birth_day', css_class = 'birth-day-class'),
                                    Div('birth_year', css_class = 'birth-year-class')
                                ),
                            css_class="form-row birth-box"),

                            Div(
                                Row(
                                    Div('death_month', css_class = 'death-month-class'),
                                    Div('death_day', css_class = 'death-day-class'),
                                    Div('death_year', css_class = 'death-year-class')
                                ),
                            css_class="form-row death-box"),

                        css_class = 'dims-row'))),
            
            css_class='box-7'),


            Div(
            
                Div(
                    Div(
                        HTML("<p><strong>Bio"), 
                        css_class='bio-label'),
                    css_class='form-row bio-label-box'),

                Row(
                    Div(
                        Field('bio'), 
                    css_class='description-class-bio')),

                Div(
                    Div(
                        HTML("<p><strong>Notes"), 
                        css_class='notes-label'),
                css_class='form-row bio-label-box'),

            Row(
                Div(
                    Field('notes'), 
                    css_class='description-class-notes')),

            css_class='box-8'),

            Div(
                    Row(
                        Div(HTML('<button type="button" class="btn btn-primary" style="margin-bottom: 50px; padding: 10px 150px 10px 100px; text-align: center; border: 1px solid #D3D3D3; border-radius: 25px 25px 25px 25px; color: white; background-color: #D3D3D3; width: 25px; height: 45px; font-size: 15px;"><strong>Cancel</strong></button>'),
                        css_class = 'cancel'),
                        Div(HTML('<button type="button" class="btn btn-warning ml-4" style="padding: 5px 150px 15px 100px; text-align: center; border: 1px solid #D3D3D3; border-radius: 25px 25px 25px 25px; color: white; ; width: 35px; height: 45px; font-size: 20px; background-color: #00CC33;">Save</button>'),
                        css_class = 'submit'),
                    ),
                css_class = 'btn-row',
                ),
        
        )#end layout
        
        
        #also sort of works
    
    def clean_uploader(self):
        if not self.cleaned_data['uploader']:
            return User()
        return self.cleaned_data['uploader']





                        ## end test ##