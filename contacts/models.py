from django.db import models
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

import uuid

from shortuuidfield import ShortUUIDField

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique uuid for contact')
    
    first_name = models.CharField(max_length=200, default='First Name')
    
    middle_name = models.CharField(max_length=200, default='Middle Name')
    
    last_name = models.CharField(max_length=200, default='Last Name')
    
    job_title = models.CharField(max_length=200, null=True, blank=True, default='Job Title')
    
    #company = models.CharField(max_length=200, null=True, blank=True, default='Company')
    company = models.CharField(max_length=200, null=True, blank=True, default='Company')

    
    email = models.CharField(max_length=200, null=True, blank=True, default='Email')
    
    phone_number = models.CharField(max_length=200, null=True, blank=True, default='Phone Number')
    
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True) #not working
    death_date = models.DateField(null=True, blank=True)
    
    bio = models.TextField(max_length=1000, null=True, blank=True, default='Bio')
    notes = models.TextField(max_length=1000, null=True, blank=True, default='Notes')


    ##01/09/22
    birth_year = models.CharField(max_length=4, default="YY")
    birth_month = models.CharField(max_length=2, default="MM")
    birth_day = models.CharField(max_length=2, default="DD")

    death_year = models.CharField(max_length=4, default="YY")
    death_month = models.CharField(max_length=2, default="MM")
    death_day = models.CharField(max_length=2, default="DD")


    ##01/19/22
    city = models.CharField(max_length=50, default='city')
    state = models.CharField(max_length=5, null=True, blank=True, default='state')
    zip_code = models.CharField(max_length=10, null=True, blank=True, default='zip')


    CONTACT_TYPES = (
        ('Work', 'WORK'),
        ('Home', 'HOME'),
        ('Other', 'OTHER'),
        #('none', 'NONE'),
    )

    contact_types = models.CharField(
        max_length=5,
        choices=CONTACT_TYPES,
        blank=False,
        default='WORK',
        help_text='',
    )

    contact_image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
       return reverse('detail', args=[str(self.id)])

#    def __str__(self):
#        return '{0}, {1}'.format(self.id, self.first_name)

    def __str___(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
    
#    def get_absolute_url(self):
#        return HttpResponseRedirect(reverse('contacts-detail', args=[str(self.id)]))



                        ### test ###

##1/9/22
def upload_contact_image(instance, filename):
    return f"images/{instance.data.title}/contacts/{filename}"


class ContactImage(models.Model):
    image = models.ImageField(upload_to=upload_contact_image)
    data = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="images")
    #data = models.ForeignKey(NewPiece2, on_delete=models.CASCADE, related_name="images")


class Company(models.Model):
    ##   ##


    #        Will have zip code etc for each model #

    city = models.CharField(max_length=50, null=True, blank=True, default='city')
    state = models.CharField(max_length=5, null=True, blank=True, default='state')
    zip_code = models.CharField(max_length=10, null=True, blank=True, default='zip')

    ## ##
    
    pass



class Contact_test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique uuid for contact')
    
    first_name = models.CharField(max_length=200, default='First Name')
    
    middle_name = models.CharField(max_length=200, default='Middle Name')
    
    last_name = models.CharField(max_length=200, default='Last Name')
    
    job_title = models.CharField(max_length=200, null=True, blank=True, default='Job Title')
    
    #company = models.CharField(max_length=200, null=True, blank=True, default='Company')
    company = models.CharField(max_length=200, null=True, blank=True, default='Company')

    
    email = models.CharField(max_length=200, null=True, blank=True, default='Email')
    
    phone_number = models.CharField(max_length=200, null=True, blank=True, default='Phone Number')
    
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True) #not working
    death_date = models.DateField(null=True, blank=True)
    
    bio = models.TextField(max_length=1000, null=True, blank=True, default='Bio')
    notes = models.TextField(max_length=1000, null=True, blank=True, default='Notes')


    ##01/09/22
    birth_year = models.CharField(max_length=4, default="YY")
    birth_month = models.CharField(max_length=2, default="MM")
    birth_day = models.CharField(max_length=2, default="DD")

    death_year = models.CharField(max_length=4, default="YY")
    death_month = models.CharField(max_length=2, default="MM")
    death_day = models.CharField(max_length=2, default="DD")


    ##01/19/22
    city = models.CharField(max_length=50, default='city')
    state = models.CharField(max_length=5, null=True, blank=True, default='state')
    zip_code = models.CharField(max_length=10, null=True, blank=True, default='zip')


    CONTACT_TYPES = (
        ('Work', 'WORK'),
        ('Home', 'HOME'),
        ('Other', 'OTHER'),
        #('none', 'NONE'),
    )

    contact_types = models.CharField(
        max_length=5,
        choices=CONTACT_TYPES,
        blank=False,
        default='WORK',
        help_text='',
    )

    contact_image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
       return reverse('detail', args=[str(self.id)])

#    def __str__(self):
#        return '{0}, {1}'.format(self.id, self.first_name)

    def __str___(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
    
                        ### end test ###

