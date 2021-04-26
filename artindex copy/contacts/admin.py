from django.contrib import admin

from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'uuid')


admin.site.register(Contact)