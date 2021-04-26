from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a borrower

import uuid  # Required for unique book instances
from shortuuidfield import ShortUUIDField

from datetime import date

# Create your models here.

##model for each piece
#only has img + title
#one-to-many w/ PaintingInstance
class Piece(models.Model):
    #model title for all instances
    #title = models.CharField(max_length=200)

    upload_name = models.CharField(max_length=200)
    
    #has many-to-one relation w/ artist
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)

    #img
    #change upload dir to 'artindex/uploads/pieces/'
    piece_upload = models.ImageField(upload_to='images/')

    #str represetations of model
    def __str__(self):
        return self.upload_name

    class Meta:
        ordering = ['artist', 'upload_name']
    
    def get_absolute_url(self):
        return reverse('piece-detail', args=[str(self.id)])

    

##model for each instance of each piece
#all other piece fields
class PieceInstance(models.Model):
    #pk
    id = models.UUIDField(primary_key=True,
    default=uuid.uuid4, help_text="Unique ID for this piece instance")

    #many to one relations
    piece = models.ForeignKey('Piece', on_delete=models.SET_NULL, null=True)

    #textfields
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, help_text="Add Description")
    medium = models.CharField(max_length=200)
    subject_matter = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    #numeric
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    #etc user enter
    date_of_upload = models.DateField(null=True, blank=True)

    #many to many relations
    #dics
    PIECE_TYPES = (
        ('painting', 'PAINTING'),
        ('sculpture', 'SCULPTURE'),
        ('textile', 'TEXTTILE'),
        ('photograph', 'PHOTOGRAPH'),
        ('none', 'NONE'),
    )

    PIECE_VISIBILITY = (
        ('Private', 'PRIVATE'),
        ('Public', 'PUBLIC'),
    )

    PIECE_AVAILABILITY = (
        ('Unfinished', 'UNFINISHED'),
        ('Complete', 'COMPLETE'),
        ('Pending', 'PENDING'),
        ('Sold', 'SOLD'),
    )

    PIECE_DIM = (
        ('inches', 'INCHES'),
        ('centimeters', 'CENTIMETERS'),
    )

    #fields
    types = models.CharField(
        max_length=10,
        choices=PIECE_TYPES,
        blank=True,
        default='none',
        help_text='type')

    visibility = models.CharField(
        max_length=10,
        choices=PIECE_VISIBILITY,
        blank=True,
        default='none',
        help_text='type')

    availability = models.CharField(
        max_length=10,
        choices=PIECE_AVAILABILITY,
        blank=True,
        default='none',
        help_text='type')

    dim = models.CharField(
        max_length=15,
        choices=PIECE_DIM,
        blank=True,
        default='none',
        help_text='type')
    
    #tags
    #unsure how to do this rn


    #model config
    class Meta:
        ordering = ['date_of_upload', 'availability']
    
    def __str__(self):
        return '{0} ({1})'.format(self.id, self.title)



##IN USE
class NewPiece(models.Model):
    #model title for all instances
    #title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True,
    default=uuid.uuid4, help_text="Unique ID for this piece instance")

    #has many-to-one relation w/ artist
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)

    #textfields
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, help_text="Add Description")
    medium = models.CharField(max_length=200)
    subject_matter = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    #numeric
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    price = models.IntegerField()
    
    #img
    #change upload dir to 'artindex/uploads/pieces/'
    piece_upload = models.ImageField(upload_to='images/')

    #etc user enter
    date_of_upload = models.DateField(null=True, blank=True)


    #many to many relations
    #dics
    PIECE_TYPES = (
        ('painting', 'PAINTING'),
        ('sculpture', 'SCULPTURE'),
        ('textile', 'TEXTTILE'),
        ('photograph', 'PHOTOGRAPH'),
        ('none', 'NONE'),
    )

    PIECE_DIM = (
        ('inches', 'INCHES'),
        ('centimeters', 'CENTIMETERS'),
    )

        
    PIECE_VISIBILITY = (
        ('Private', 'PRIVATE'),
        ('Public', 'PUBLIC'),
    )

    PIECE_AVAILABILITY = (
        ('Unfinished', 'UNFINISHED'),
        ('Complete', 'COMPLETE'),
        ('Pending', 'PENDING'),
        ('Sold', 'SOLD'),
    )

    #fields
    types = models.CharField(
        max_length=10,
        choices=PIECE_TYPES,
        blank=True,
        default='none',
        help_text='type')

    dim = models.CharField(
        max_length=15,
        choices=PIECE_DIM,
        blank=True,
        default='none',
        help_text='type')
    
    visibility = models.CharField(
        max_length=10,
        choices=PIECE_VISIBILITY,
        blank=True,
        default='none',
        help_text='type')

    availability = models.CharField(
        max_length=10,
        choices=PIECE_AVAILABILITY,
        blank=True,
        default='none',
        help_text='type')
        
    #tags
    #unsure how to do this rn

    #str represetations of model
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['artist', 'title']
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])



##end of in use##







##piece-only upload w/ dropzone
#based on:  https://www.existenceundefined.com/blog/programming/13/django-multiple-image-upload-with-dropzonejs
#           https://www.sitepoint.com/file-upload-form-express-dropzone-js/
#           https://stackoverflow.com/questions/29240246/django-and-dropzone-how-to-post-form
#
class Photo(models.Model):
    photo = models.ImageField(upload_to="images/")
    photo_compressed = models.ImageField(upload_to="images/")
    thumbnail = models.ImageField(upload_to="thumbnail/")

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        if not self.make_thumbnail(small=True):
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Photo, self).save(*args, **kwargs)

    def make_thumbnail(self, small=False):
        return make_thumbnail(self, small)



#need to download dropzone.js file?
class PieceOnly_upload(models.Model):
    file = models.ImageField(upload_to="images/")

    def __unicode__(self):
        return self.file.name






##tutorial
class NewPiece_1(models.Model):
    id = models.UUIDField(primary_key=True,
    default=uuid.uuid4, help_text="Unique ID for this piece instance")

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment = models.TextField(max_length=500)

    #str represetations of model
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'email']
    
#    def get_absolute_url(self):
#        return reverse('detail', args=[str(self.id)])









##model for each artist
class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    artist_email = models.EmailField(max_length=200)
    artist_phone = models.CharField(max_length=12, help_text="Enter phone number in format 'xxx-xxx-xxxx")

    #collections
    #list a list of pieces by each artist (via pk?)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])
    
    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)

##collection of works by each artist
class Collection(models.Model):
    pass

    #do something like this
    #def get_queryset(self):
    #    return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
