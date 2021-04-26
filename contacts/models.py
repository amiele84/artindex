from django.db import models
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

import uuid

from shortuuidfield import ShortUUIDField

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique uuid for contact')
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True) #not working
    death_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    notes = models.TextField(max_length=1000, null=True, blank=True)

    CONTACT_TYPES = (
        ('Work', 'WORK'),
        ('Home', 'HOME'),
        ('Other', 'OTHER'),
        ('none', 'NONE'),
    )

    contact_types = models.CharField(
        max_length=5,
        choices=CONTACT_TYPES,
        blank=True,
        default='none',
        help_text='type',
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




