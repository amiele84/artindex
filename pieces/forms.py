from django import forms 
from django.contrib.auth.models import User

from .models import Piece, PieceInstance, Artist, NewPiece, NewPiece2, PieceImage2

##for crispy forms/form helper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset, Row, Column, HTML


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



                ##in use##
class NewUploadForm(forms.ModelForm):
    
    class Meta:
        model = NewPiece
        fields = [
            'piece_upload','title', 'artist', 
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
        self.helper.form_show_labels = True #hides all labels
        self.helper.form_style='inline'
        self.helper.layout = Layout(

            Fieldset('Upload Piece Here',
                    Field('piece_upload', placeholder='Drag/Drop pieces here'),
            ),
            Fieldset('artist', 'title',
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price', 'tags'),
        ),
        Row(
                Column('availability', css_class='form-group col-md-6 mb-0', id='avail'),
                Column('price', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        Row(
                Column('height', css_class='form-group col-sm-2 mb-0'),
                Column('width', css_class='form-group col-sm-2 mb-0'),
                Column('depth', css_class="form-group col-sm-2 mb-0"),
                Column('dim', css_class="form-group col-sm-2 mb-0"),
                css_class='form-row',
                css_id='dims'
            ),
        Row(
                Column('piece_upload', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
        )
        Row(
                Column('tags', css_class='form-group col-md-4 mb-0')
        ),

        

        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean_uploader(self):
        if not self.cleaned_data['uploader']:
            return User()
        return self.cleaned_data['uploader']



                    ## end of in use ##



                    ## start of test ##
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

###8/8
class PicDataForm(forms.Form):
    favorite_food = forms.CharField(
        label = 'What your fav food', #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'EEEEE'
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_show_labels = True #hides all labels
        
        
        self.helper.layout = Layout(

            #sets order of fields on page
            Fieldset(
                'first arg is the legend of the fieldset',
                'favorite_color',
                'favorite_food',
                'notes',
            ),
            
            Div(
                'favorite_food',
                'favorite_number',
                css_id = 'special-fields',
                css_class = 'special-class',
            ),
        )


### 8/19 
#tutorial: https://engineertodeveloper.com/how-to-build-a-photo-gallery-with-django-part-1/
from .models import PicOnly, DataOnly
class DataForm(forms.ModelForm):
    class Meta:
        model = DataOnly
        fields = ('title',)


class PicOnlyForm(forms.ModelForm):
    class Meta:
        model = PicOnly
        fields = ('upload_pic',)


### 8/23
#taking actual code from: https://github.com/EngineerToDeveloper/photo-gallery-tutorial/blob/main/pages/forms.py
from .models import Pet, Image

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)


###9/24
#combining new1/ w/ pet
from .models import UploadPiece, PieceImage

class UploadPieceForm(forms.ModelForm):
    class Meta:
        model = UploadPiece
        fields = ('title',)


class PieceImageForm(forms.ModelForm):
    class Meta:
        model = PieceImage
        fields = ('image',)




### 8/25
class TestForm(forms.Form):
    
    TYPES_CHOICES =(
        ("1", "None"), #default value
        ("2", "Sculpture"),
        ("3", "Textile"),
        ("4", "Photograph"),
        ("5", "Painting"),
        )

    VISIBILITY_CHOICES =(
        ("1", "Public"), #default value
        ("2", "Private"),
        )

    piece_title = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add title',
    )

    ####left side
    ###8/26
    #code: http://www.learningaboutelectronics.com/Articles/How-to-create-a-text-area-in-a-Django-form.php

    
    ##typed choice field
    piece_artist = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add Artist',
    )

    piece_description = forms.CharField(
        initial = 'Add Description',
        label = False,
        widget=forms.Textarea(
            attrs={"rows":6, "cols":15}
            ), #can add attributes
    )

    types_field = forms.ChoiceField(
        label = False,
        choices = TYPES_CHOICES,
        )
    
    ###8/28
    medium_field = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add Medium',
    )

    subject_matter_field = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add Subject Matter',
    )


    date_of_upload_field = forms.CharField(
        label = False,
        initial = 'mm/dd/yyyy'
    )

    #can't format right
    month_field = forms.CharField(
        label = False,
        initial = "MM"
    )

    day_field = forms.CharField(
        label = False,
        initial = "DD"
    )
    
    year_field = forms.CharField(
        label = False,
        initial = "YYYY"
    )

    visibility_field = forms.ChoiceField(
        label = False,
        choices = VISIBILITY_CHOICES,
        )

    ####right side
    ###8/28
    height_field = forms.IntegerField(
        label = False,
    )

    width_field = forms.IntegerField(
        label = False,
    )

    depth_field = forms.IntegerField(
        label = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        
            #trying to get 2 cols
            Div(
                Column(
                    Row(
                        Div(
                            'piece_title',
                            css_id = 'title-field',
                            css_class = 'title-class',
                            ),
                        css_class = 'row1-class',
                    ), #end row1
                ),

                Column(
                    'piece_title',
                    css_class = 'title-class'
                ),
                

                Row(
                    Div(
                        'piece_description',
                        css_id = 'description-field',
                        css_class = 'description-class',
                        ),

                css_class = 'row2-class',
                ), #end row2

                Column(
                    'piece_title',
                ),
            ),

            Div(
                'piece_title',
                css_id = 'title-field',
                css_class = 'title-class',
            ),
            Div(
                'piece_description',
                css_id = 'description-field',
                css_class = 'description-class',
            ),

            Div(
                'piece_artist',
                css_id = 'artist-field',
                css_class = 'artist-class',
            ),

            Div(
                'types_field',
                css_id = 'types-field',
                css_class = 'types-class',
            ),

            Div(
                'medium_field',
                css_id = 'medium-field',
                css_class = 'medium-class',
            ),

            Div(
                'subject_matter_field',
                css_id = 'subject-matter-field',
                css_class = 'subject-matter-class',
            ),

            Div(
                Row(
                    #single
                    Column(
                        'date_of_upload_field',
                        css_id = 'date-field',
                        css_class = 'date-class',
                    ),
                    #three separate
                    #Column(
                    #    'month_field',
                    #    'day_field',
                    #    'year_field',
                    #    css_id = 'date-field',
                    #    css_class = 'date-class',
                    #),

                    Column(
                        'visibility_field', 
                        css_id = 'visibility-field',
                        css_class = 'visibility-class',
                    ),
                    
                css_class='form-row',
                css_id=''
                ),
            ),

            ##how to get horizonal stuff
            Div(
                Row(
                    Column('month_field'),
                    Column('day_field'),
                    Column('year_field'),
                    css_class = 'title-class',
                )
            ),

        )#end layout


### 8/29
##copy of test form for playing w/
from django.utils.translation import ugettext_lazy as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from taggit.managers import TaggableManager
from django.db import models

class TestForm2(forms.Form):
    
    TYPES_CHOICES =(
        ("1", "None"), #default value
        ("2", "Sculpture"),
        ("3", "Textile"),
        ("4", "Photograph"),
        ("5", "Painting"),
        )

    VISIBILITY_CHOICES =(
        ("1", "Public"), #default value
        ("2", "Private"),
        )

    DIMS_CHOICES = (
        ('inches', 'INCHES'),
        ('centimeters', 'CENTIMETERS'),
    )

    AVAILABILITY_CHOICES = (
        ('Unfinished', 'UNFINISHED'),
        ('Complete', 'COMPLETE'),
        ('Pending', 'PENDING'),
        ('Sold', 'SOLD'),
    )

    piece_title = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add title',
    )

    ####left side
    #code: http://www.learningaboutelectronics.com/Articles/How-to-create-a-text-area-in-a-Django-form.php
    
    ##typed choice field
    piece_artist = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add Artist',
    )

    piece_description = forms.CharField(
        initial = 'Add Description',
        label = False,
        widget=forms.Textarea(
            attrs={"rows":6, "cols":15}
            ), #can add attributes
    )

    piece_types = forms.ChoiceField(
        label = False,
        choices = TYPES_CHOICES,
        )
    

    piece_medium = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add Medium',
    )

    piece_subject_matter = forms.CharField(
        label = False, #if False, removes form label
        max_length = 80,
        required = True,
        initial = 'Add Subject Matter',
    )


    piece_date = forms.CharField(
        label = False,
        initial = 'mm/dd/yyyy'
    )

    #can't format right
    piece_month = forms.CharField(
        label = False,
        initial = "MM"
    )

    piece_day = forms.CharField(
        label = False,
        initial = "DD"
    )
    
    piece_year = forms.CharField(
        label = False,
        initial = "YYYY"
    )

    piece_visibility = forms.ChoiceField(
        label = False,
        choices = VISIBILITY_CHOICES,
        )


    piece_location = forms.CharField(
        label = False,
        initial = 'Add Location'
    )

    ####right side
    piece_height = forms.IntegerField(
        label = False,
    )

    piece_width = forms.IntegerField(
        label = False,
    )

    piece_depth = forms.IntegerField(
        label = False,
    )

    piece_dims = forms.ChoiceField(
        label = False,
        choices = DIMS_CHOICES,
        )

    piece_availability = forms.ChoiceField(
        label = False,
        choices = AVAILABILITY_CHOICES,
        )
    
    piece_price = forms.IntegerField(
        label = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        
            #trying to get 2 cols
            Div(
                Column(
                    Row(
                        Column('piece_title', css_class = 'title-class'),
                        Column('piece_description'),
                        Column('piece_medium'),
                        Column('piece_subject_matter'),
                        Column('piece_location'),
                        Column('piece_date'),
                        Column('piece_visibility'),
                        css_class = 'row1-class',
                        ),
                    ),
                Column(
                    Row(
                        Column('piece_width'),
                        Column('piece_height'),
                        Column('piece_depth'),
                        Column('piece_dims'),
                        Row('piece_availability'),
                        Column('piece_price'),
                        css_class = 'row2-class',
                        ),
                    ), 
                ),
            )#end layout





 ###9/1
 ##just NewFormUpload copies


###/9/1
#NewFormUpload copy
from django.urls import reverse_lazy #1
from django.forms import Textarea, CharField

class TestForm3(forms.ModelForm):

    class Meta:
        model = NewPiece
        fields = [
            'piece_upload','title', 'artist', 
            'description', 'types', 'medium',
            'subject_matter', 'location', 'month', 'day', 'year', #'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price','tags', 'edition_num', 'edition_dom',
            ]
        
        widgets = {
            'description': Textarea(attrs={'cols': 100, 'rows': 5}), #12-27
        }
    #tags
    #use "MultiValueField"

    ##form helper
    ##adapted from: https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
    def __init__(self, *args, **kwargs):
        super(TestForm3, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id_new_upload_form'
        self.helper.form_class = 'uploadForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'uploadpiece' #where submit redirects to
        self.helper.form_show_labels = False #hides all labels
        self.helper.form_style='inline'
        self.helper.layout = Layout(
        
            #trying to get 2 cols
            #Div(
            #    Column(
            #        Row('title', css_class = 'title-class'),
            #        Row('description', css_class = 'description-class'),
            #        Row('types', css_class = 'types-class'),
            #    )
            #),
            #Field('title', ), #12-25
            Row(
                Div(
                    Row(
                        ###9/7 changed from 'row' to 'div'
                        Column(
                            #Div(Field('title'), css_class = 'title-class'), #12-25
                            #Div('title', css_class = 'title-class'),
                            #Div('description', css_class=  'description-class'),
                            
                            #12-27
                            Div(
                                Row(
                                    Div('title', css_class = 'title-class')
                                ),
                                Row(
                                    Div(Field('description'), css_class=  'description-class')
                                ),
                            css_class = 'first-box'
                            ),

                            Div(
                                Row(HTML("<p><span style='padding-left: 25px; font-size: 15px;'><strong>Type</strong></span></p>")), #12-27
                                Field('types', css_class = 'types-class'),
                                css_class = 'types-row',
                            ),
                            
                            Div(
                                Row(
                                    Div('medium', css_class = 'medium-class'), 
                                    css_class='medium-row',
                                ),
                                Row(
                                    Div('subject_matter', css_class = 'subject-matter-class'), 
                                    css_class='subject-matter-row',
                                ),
                                Row(
                                    Div('location', css_class = 'location-class'), 
                                    css_class='location-row',
                                ),
                            css_class = 'third-box'
                            ),
                            
                            #Div('medium', css_class = 'medium-class'),
                            #Div('subject_matter', css_class = 'subject-matter-class'),
                            #Div('location', css_class = 'location-class'),
                            
                            Div(
                                Row(
                                    Column(
                                        HTML("<p><span style='font-size: 15px;'><strong>Creation Date</strong></span></p>"), css_class = 'date-label-class'),
                                    Column(
                                        HTML("<p><span style='font-size: 15px; padding-left: 20px;'><strong>Visibility</strong></span></p>"), css_class = 'visibility-label-class'),
                                css_class='label-row-2'
                                ),
                                Row(
                                    Column(
                                        Row(
                                            Div('month', css_class = 'width-class'),
                                            Div('day', css_class = 'height-class'),
                                            Div('year', css_class = 'depth-class'),
                                        css_class = 'dims-row'
                                        ),
                                    ),
                                Column(
                                    Div('visibility', css_class = 'visibility-class'),
                                    ),
                                ),
                                Div(
                                    Div(
                                        Row(
                                            HTML('<div class="form-check" style="font-size: 15px;"><span><p><label class="form-check-label" for="flexCheckChecked"><strong>Signature</strong></label></div>'),
                                            css_class = 'signature-label'
                                            ),
                                        Row(
                                            HTML('<div class="form-check"><p><input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked></div>'),
                                            css_class = 'signature-checkbox'
                                            ),
                                    css_class = 'signature-box'
                                    ),
                                css_class = 'fourth-box'
                                ),
                            css_class = 'left-side-row',
                            ),
                            
                        ),
                     css_class = 'left-side-column',
                    ),
                css_class = 'left-side-row'
                ),

                Div(
                    Column(
                        Div(
                            HTML("<div style='font-size: 15px; padding-bottom: 0px;'><p><span><strong>Dimensions</strong></span></p></div>"), 
                            css_class = 'dim-label-class'
                            ),
                        Column(
                            Row(
                                Div('width', css_class = 'width-class'),
                                Div('height', css_class = 'height-class'),
                                Div('depth', css_class = 'depth-class'),
                                #Div('dim', css_class = 'dim-class'),

                                Div(
                                    Div(
                                        HTML('<select class="form-select" aria-label="Default select example"><option selected>Inches</option><option value="1">Inches</option><option value="2">cm</option><option value="3">m</option></select>'),
                                css_class = 'price-type-class'),
                                ),
                            css_class = 'dims-row'
                            ),
                            Row(
                                HTML("<p><strong>+ Add Framed Size"), 
                                css_class = 'add-frame-row'
                            ),
                            Row(
                                Row(
                                    HTML("<p><span style='font-size: 15px;'><strong>Status</strong></span></p>"), 
                                    css_class = 'status-label-class'
                                ),
                            ),
                            Row(
                                Div('availability', css_class = 'availability-class'),
                                Div('price', css_class = 'price-class'),
                                Div(
                                    HTML('<select class="form-select" aria-label="Default select example"><option selected>USD$</option><option value="1">One</option><option value="2">Yen¥</option><option value="3">GBP £</option></select>'),
                                css_class = 'price-type-class'
                                ),
                            css_class = 'avail-row'
                            ),
                            
                            Div(
                                Row(
                                    Div('tags', css_class = 'tag-class'),
                                css_class="tag-row"
                                ),
                                Row(
                                    Div(HTML('<div class="tag-box mb-3"><textarea class="form-control" id="exampleFormControlTextarea1" rows="4"></textarea></div>'), 
                                    css_class="tag-box-class"
                                    ),
                                ),
                            ),
                        css_class = 'fifth-box',
                        ),

                    Div(
                        Row(
                            Column(
                                Div(
                                    HTML('<div class="col"><div class="form-check"><span"><p><label class="form-check-label" for="flexCheckChecked" style="font-size: 15px;"><strong>Editions</strong></label></div></div>'),
                            css_class = 'edition-label'),
                            ),
                        ),
                    css_class='exhibtion-check-col'
                    ),

                    Div(
                        Row(
                            Column(
                                Div(
                                    HTML('<div class="col" style="padding-left: 70px; padding-right: 30px;"><div class="form-check"></span><p><input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked></div></div>'),
                                css_class = 'edition-checkbox')
                                ),
                            Row(
                                Div('edition_num', css_class = 'edition-num-class'),
                                Div(HTML('<span style="padding-top: 20px;"><p style="font-size: 20px; padding-top: 10px; padding-left: 25px; padding-right: 25px;">/</p></span>')),
                                Div('edition_dom', css_class = 'edition-num-class'),
                            ),
                        ),
                    css_class='edition-split-class',
                    ),
                    css_class = 'right-side-column',
                    ),
                css_class = 'right-side-divison',
                ),

                Div(
                    Row(
                        Div(HTML('<button type="button" class="btn btn-primary" style="margin-bottom: 50px; padding: 10px 150px 10px 100px; text-align: center; border: 1px solid #D3D3D3; border-radius: 25px 25px 25px 25px; color: white; background-color: #D3D3D3; width: 25px; height: 45px; font-size: 15px;"><strong>Cancel</strong></button>'),
                        css_class = 'cancel'),
                        Div(HTML('<button type="button" class="btn btn-warning ml-4" style="padding: 5px 150px 15px 100px; text-align: center; border: 1px solid #D3D3D3; border-radius: 25px 25px 25px 25px; color: white; ; width: 35px; height: 45px; font-size: 20px; background-color: #00CC33;">Save</button>'),
                        css_class = 'submit'),
                    ),
                css_class = 'btn-row',
                ),

            css_class = 'container-6'
            ),
            
            )#end layout

        
        #also sort of works
    
    def clean_uploader(self):
        if not self.cleaned_data['uploader']:
            return User()
        return self.cleaned_data['uploader']



##10/11
from .models import GeeksModel

# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
            "upload_pic"]


###10/28###
##pic upload form
class PieceImageForm2(forms.ModelForm):
    class Meta:
        model = PieceImage2
        fields = ('image',)


##no piece upload, separate form
class TestForm4(forms.ModelForm):

    class Meta:
        model = NewPiece2
        fields = [
            'title', 'artist', 
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
        super(TestForm4, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id_new_upload_form'
        self.helper.form_class = 'uploadForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'boobies' #where submit redirects to
        self.helper.form_show_labels = False #hides all labels
        self.helper.form_style='inline'
        self.helper.layout = Layout(
        
            #trying to get 2 cols
            #Div(
            #    Column(
            #        Row('title', css_class = 'title-class'),
            #        Row('description', css_class = 'description-class'),
            #        Row('types', css_class = 'types-class'),
            #    )
            #),
            Row(
                Div(
                    Column(
                        ###9/7 changed from 'row' to 'div'
                        Column(
                            Div('title', css_class = 'title-class'),
                            Div('description', css_class=  'description-class'),
                            Div('types', css_class = 'types-class'),
                            Div('medium', css_class = 'medium-class'),
                            Div('subject_matter', css_class = 'subject-matter-class'),
                            Div('location', css_class = 'location-class'),
                            Row(
                                Div('date_of_upload', css_class = 'date-class'),
                                Div('visibility', css_class = 'visibility-class'),
                            ),
                        css_class = 'left-side-row',
                        ),
                    css_class = 'left-side-column',
                    ),
                css_class = 'left-side-divison'
                ),

                Div(
                    Column(
                        Column(
                            Row(
                                Div('width', css_class = 'width-class'),
                                Div('height', css_class = 'height-class'),
                                Div('depth', css_class = 'depth-class'),
                                Div('dim'),
                            ),
                            Row(
                                Column('availability', css_class = 'availability-class'),
                                Column('price', css_class = 'price-class'),
                            ),
                            Row(
                                Column('tags', css_class = 'tags-class'),
                            ),
                        css_class = 'right-side-row',
                        ),
                    css_class = 'right-side-column',
                    ),
                css_class = 'right-side-divison',
                ),
            css_class = 'full-form-class'
            ),     
        )#end layout

        
        #also sort of works
        self.helper.add_input(Submit('submit', 'Submit', css_class = 'btn-row-class'))
    
    def clean_uploader(self):
        if not self.cleaned_data['uploader']:
            return User()
        return self.cleaned_data['uploader']
## end of test ##





                


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
 