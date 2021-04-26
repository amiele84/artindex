import django_tables2 as tables

import itertools

from .models import Piece, PieceInstance, NewPiece


            ## tables for pieces list ##

#table for large list
#sequence: img/title
class PiecesTableLarge(tables.Table):
    model = Piece
    sequence = ('piece_upload', 'title')
    
    #attrs = {"class": 'pieces_table'}
    #template_name = "django_tables2/bootstrap.html"
    #fields = ("piece_upload", "title")

#table for medium list
#sequence: [
    #[img],
    #[title, description, materials, availability, price,] 
    #[type: type,], 
    #[size:size, subject: [s1, s2...etc], 
    #location:location],
    #[tags],
    #]
class PiecesTableMedium(tables.Table):
    model = NewPiece
    #sequence = (
    #    ['piece_upload'], ['artist']
    #    ['title', 'description', 'medium','availability', 'price'],
    #    ['types'],
    #    ['dim', 'subject_matter', 'location'],
    #    ['width', 'height', 'depth'],
    #    ['price'],
    #)

#table for detail view
#sequence: 
    #[img, title, materials, availbility, price, "..."]
class PiecesTableDetail(tables.Table):
    model = PieceInstance
    sequence = ('piece_upload', 'title', 'medium', 'avalability')



    