from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a borrower

from django_mysql.models import ListCharField

import uuid  # Required for unique book instances
from shortuuidfield import ShortUUIDField

from datetime import date

from taggit.managers import TaggableManager

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


            ## ##









from django.utils.translation import ugettext_lazy as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

            ##in USE ##

class Tag(models.Model):
    tag = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.tag)



class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    #tag = models.ForeignKey('Tag', related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")



from datetime import date
from django.core import validators
#from validators import maxValueValidator

class NewPiece(models.Model):

    #model title for all instances
    #title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True,
    default=uuid.uuid4, help_text="Unique ID for this piece instance")

    #has many-to-one relation w/ artist
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, blank=True)

    #has many-to-one relation with uploader
    #currently just entering "username" as field 
    #should work just based on upload
    #currently a workaround 
    #uploader = models.CharField(max_length=200)
    #user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    #uploader = models.ForeignKey(User, related_name ="newpiece_creator_set", on_delete=models.CASCADE) #default=User, null=True, blank=True, on_delete=models.CASCADE)#, null=True)
    
    
    #textfields
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=True)
    medium = models.CharField(max_length=200, blank=True)
    subject_matter = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    #numeric
    #today = date.today()
    #year = models.IntegerField(validators=[validators.MaxValueValidator(9999)], default=today.year)
    #month = models.IntegerField(validators=[validators.MaxValueValidator(99)], blank=False,default=today.month)
    #day = models.IntegerField(validators=[validators.MaxValueValidator(99)], blank=False, default=today.day)

    year = models.CharField(max_length=4, default="YY")
    month = models.CharField(max_length=2, default="MM")
    day = models.CharField(max_length=2, default="DD")

    #width = models.IntegerField(blank=True)
    #height = models.IntegerField(blank=True)
    #depth = models.IntegerField(blank=True)

    width = models.CharField(max_length=3, default="W")
    height = models.CharField(max_length=3, default="H")
    depth = models.CharField(max_length=3, default="D")

    #price = models.IntegerField(blank=True)
    price = models.CharField(max_length=10, blank=False, default='Add Price')

    #edition_num = models.IntegerField(blank=False, default=00) #12-27
    #edition_dom = models.IntegerField(blank=False, default=00) #12-27
    
    edition_num = models.CharField(max_length=3, default='000') #12-27
    edition_dom = models.CharField(max_length=3, default='000') #12-27
    
    #img
    #change upload dir to 'artindex/uploads/pieces/'
    piece_upload = models.ImageField(upload_to='images/')

    #etc user enter
    date_of_upload = models.DateField(null=True, blank=True)


    #many to many relations
    #dics
    PIECE_TYPES = (
        #('Add Type', 'ADD TYPE'), #12-27
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
        blank=False,
        default = 'painting')

    dim = models.CharField(
        max_length=15,
        choices=PIECE_DIM,
        blank=False,
        default = 'inches')
    
    visibility = models.CharField(
        max_length=10,
        choices=PIECE_VISIBILITY,
        blank=False,
        default = 'PRIVATE')

    availability = models.CharField(
        max_length=10,
        choices=PIECE_AVAILABILITY,
        blank=False,
        default='Unfinished')
        
    #tags
    #unsure how to do this rn
    tags = TaggableManager(through=UUIDTaggedItem, blank=True, help_text = "")

    #str represetations of model
    def __str__(self):
        return self.title
    
    #test
    @property
    def is_today(self):
        if date_of_upload == date.today():
            return True
        return False

    class Meta:
        ordering = ['artist', 'title']
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


                ##end of in use##
 



                ## test ##

#piece-dta-only class
class DataOnly(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title 



#pic only class
class PicOnly(models.Model):
    upload_pic = models.ImageField(upload_to='images/')
    piece = models.ForeignKey(DataOnly, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def __str__(self):
        return str(self.pk)



###8/23
#using actual code from: https://github.com/EngineerToDeveloper/photo-gallery-tutorial/blob/main/pages/models.py
class Pet(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

def upload_gallery_image(instance, filename):
    return f"images/{instance.pet.name}/gallery/{filename}"

class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="images")



###9/25
#combining new1/ w/ pet
class UploadPiece(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.name



def upload_piece_image(instance, filename):
    return f"images/{instance.data.title}/gallery/{filename}"


class PieceImage(models.Model):
    image = models.ImageField(upload_to=upload_piece_image)
    data = models.ForeignKey(UploadPiece, on_delete=models.CASCADE, related_name="images")
    #data = models.ForeignKey(NewPiece2, on_delete=models.CASCADE, related_name="images")


##10/11##
#from: https://www.geeksforgeeks.org/update-view-function-based-views-django/
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    upload_pic = models.ImageField(upload_to='GeeksModels/images/', blank=True) #10/12
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


##10/26##
class NewPiece2(models.Model):
    #model title for all instances
    #title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True,
    default=uuid.uuid4, help_text="Unique ID for this piece instance")

    #has many-to-one relation w/ artist
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, blank=True)

    #has many-to-one relation with uploader
    #currently just entering "username" as field 
    #should work just based on upload
    #currently a workaround 
    #uploader = models.CharField(max_length=200)
    #user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    #uploader = models.ForeignKey(User, related_name ="newpiece_creator_set", on_delete=models.CASCADE) #default=User, null=True, blank=True, on_delete=models.CASCADE)#, null=True)
    
    
    #textfields
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=True)
    medium = models.CharField(max_length=200, blank=True)
    subject_matter = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    #numeric
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    depth = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    
    #img
    #change upload dir to 'artindex/uploads/pieces/'
    #piece_upload = models.ImageField(upload_to='images/')

    #etc user enter
    date_of_upload = models.DateField(null=True, blank=True)


    #many to many relations
    #dics
    PIECE_TYPES = (
        ('Add Type', 'ADD TYPE'),
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
        blank=False,
        default = 'UNFINISHED')

    dim = models.CharField(
        max_length=15,
        choices=PIECE_DIM,
        blank=True)
    
    visibility = models.CharField(
        max_length=10,
        choices=PIECE_VISIBILITY,
        blank=False,
        default = 'PRIVATE')

    availability = models.CharField(
        max_length=10,
        choices=PIECE_AVAILABILITY,
        blank=False,
        default='Unfinished')
        
    #tags
    #unsure how to do this rn
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)

    #str represetations of model
    def __str__(self):
        return self.title
    
    #test
    @property
    def is_today(self):
        if date_of_upload == date.today():
            return True
        return False

    class Meta:
        ordering = ['artist', 'title']
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


#taking GeeksModel and mixing with multiple upload models above
class PieceImage2(models.Model):
    image = models.ImageField(upload_to=upload_piece_image)
    data = models.ForeignKey(NewPiece2, on_delete=models.CASCADE, related_name="images")


## end of test ##













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
