from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView

from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin

from .models import *
from .tables import ContactsTable
from .forms import *

# Create your viws here.

##contact specific detail views 
class ContactsDetailView(generic.DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'

##update contact
class ContactsUpdateView(generic.UpdateView):
    model = Contact
    fields = ['first_name', 'last_name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('contacts:contacts')

#delete contact
class ContactsDeleteView(DeleteView):
    model = Contact
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('contacts:contacts')

##list of contacts
class ContactsListView(generic.ListView):
    table_class = ContactsTable
    model = Contact
    template_name = "contacts/contact_list.html"
    #context_object_name = "contacts"


##new contact view
class NewContactloadView(TemplateView):
    form = NewContactUploadForm
    template_name = 'contacts/new_contact.html'

    def post(self, request, *args, **kwargs):

        form = NewContactUploadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('contacts:contacts'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)