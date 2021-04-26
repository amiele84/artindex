from django.contrib import admin

from .models import Piece, PieceInstance, Artist, Collection, NewPiece
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