from django.contrib import admin

from .models import Piece, PieceInstance, Artist, Collection, NewPiece, PicOnly, DataOnly, GeeksModel
from .forms import *

class NewPieceAdmin(admin.ModelAdmin):
    form = NewUploadForm
    list_display = ('title', 'uploader')
    fieldsets = [
        (None, { 'fields': [('piece_upload','artist', 'title',
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price')] } ),
    ]

    def save_model(self, request, obj, form, change):
        if not obj.uploader.id:
            obj.uploader = request.user
        obj.save()

# Register your models here.
admin.site.register(Piece)
admin.site.register(PieceInstance)
admin.site.register(NewPiece)
admin.site.register(Artist)
admin.site.register(Collection)
admin.site.register(DataOnly)
admin.site.register(PicOnly)
admin.site.register(GeeksModel) #10/11



                    #### test ####

###8/23
from .models import Pet, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


###9/24
#combining new1/ w/ pet
from .models import UploadPiece, PieceImage

class PieceImageInline(admin.TabularInline):
    model = PieceImage

@admin.register(UploadPiece)
class UploadPieceAdmin(admin.ModelAdmin):
    inlines = [
        PieceImageInline
    ]




                    #### end test ####