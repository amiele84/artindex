import django_tables2 as tables

import itertools

from .models import Contact

class ContactsTable(tables.Table):
    model = Contact
    sequence = ('contact_image', 'first_name', 'last_name', 'email',
    'Phone Number', 'job_title', 'Company')