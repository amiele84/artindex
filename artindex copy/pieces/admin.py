from django.contrib import admin

from .models import Piece, PieceInstance, Artist, Collection, NewPiece

# Register your models here.
admin.site.register(Piece)
admin.site.register(PieceInstance)
admin.site.register(NewPiece)
admin.site.register(Artist)
admin.site.register(Collection)