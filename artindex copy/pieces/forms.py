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
    fields = [
        'title','description', 'types', 'medium',
        'subject_matter', 'location', 'date_of_upload',
        'visibility', 'width', 'height', 'depth', 'dim',
        'availability', 'price'
        ]

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
 