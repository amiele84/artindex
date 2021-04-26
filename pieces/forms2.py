from django import forms 
from .models import Piece, PieceInstance, Artist, NewPiece


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
            'availability', 'price'
            ]
    #tags
    #use "MultiValueField"

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
    
