from django import forms 
from .models import *



class NewContactUploadForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        
        ##birth_date & death_date don't work##
        fields = [
            'first_name', 'middle_name', 'last_name',
            'job_title', 'company', 'email', 'phone_number',
            'bio', 'notes','contact_types', 'contact_image',
            ]
        