from django import forms 
from django.contrib.auth.models import User

from .models import Piece, PieceInstance, Artist, NewPiece

##for crispy forms/form helper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset, Row, Column


#form for new img upload
#fields for title, img
class PieceOnly(forms.ModelForm):
    model = NewPiece
    fields = [
        'piece_upload', 'title'
    ]

class NewPieceInfo(forms.ModelForm):
    model = NewPiece
    fields = "__all__"



##in use
class NewUploadForm(forms.ModelForm):
    
    class Meta:
        model = NewPiece
        fields = [
            'piece_upload','artist', 'title',
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price','tags',
            ]
    #tags
    #use "MultiValueField"

    ##form helper
    ##adapted from: https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
    def __init__(self, *args, **kwargs):
        super(NewUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id_new_upload_form'
        self.helper.form_class = 'uploadForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'upload_piece'
        self.helper.layout = Layout(
            Fieldset('Upload Piece Here',
                    Field('piece_upload', placeholder='Drag/Drop pieces here'),
            ),
            Fieldset('artist', 'title',
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price', 'tags')
        ),
        Row(
                Column('availability', css_class='form-group col-md-6 mb-0'),
                Column('price', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        Row(
                Column('height', css_class='form-group col-sm-2 mb-0'),
                Column('width', css_class='form-group col-sm-2 mb-0'),
                Column('depth', css_class="form-group col-sm-2 mb-0"),
                Column('dim', css_class="form-group col-sm-2 mb-0"),
                css_class='form-row'
            ),
        Row(
                Column('piece_upload', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
        )
        Row(
                Column('tags', css_class='form-group col-md-4 mb-0')
        )
        

        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean_uploader(self):
        if not self.cleaned_data['uploader']:
            return User()
        return self.cleaned_data['uploader']


##piece dropzone form
#adapted from:  https://github.com/jazzband/django-formtools/blob/master/docs/wizard.rst
class PieceUploadOnlyForm(forms.Form):
    piece_to_upload = forms.ImageField()






##one possible method of getting css & forms
class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class' : 'myemailclass'}))
      comment = forms.CharField(widget=forms.Textarea)


##tutorial: https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html#reusing-form-components
class ContactForm_Tutorial(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm_Tutorial, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')



##test: https://www.geeksforgeeks.org/render-django-form-fields-manually/
class InputForm(forms.Form): 
  
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput())
    















#form for new piece info
#all additional data
class NewPieceCreateForm(forms.ModelForm):
    
    class Meta:
        model = NewPiece
        fields= [
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price'
        ]


#form for new artists
class NewArtistCreateForm(forms.ModelForm):

    class Meta:
        model = Artist 
        fields = [
            'first_name', 'last_name',
            'artist_email', 'artist_phone'
        ]
 