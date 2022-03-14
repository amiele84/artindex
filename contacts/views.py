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
from .filters import *

# Create your viws here.

        ##in use##

##contact specific detail views 
class ContactsDetailView(generic.DetailView):
    model = Contact
    template_name = 'contacts/contact_detail_working_copy.html'




##update contact
class ContactsUpdateView(generic.UpdateView):
    model = Contact
    fields = [
            'contact_image', 'first_name', 'middle_name', 'last_name',
            'job_title', 'company', 'email', 'phone_number',
            'bio', 'notes','contact_types',
            'birth_date', 'death_date',
            ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('contacts:contacts')




#delete contact
class ContactsDeleteView(DeleteView):
    model = Contact
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('contacts:contacts')




##list of contacts
class ContactsListView(LoginRequiredMixin, FilterView):
    table_class = ContactsTable
    model = Contact
    template_name = "contacts/contacts_list_final_working_copy.html"
    #template_name = "contacts/contacts_list_final_in_use.html"
    context_object_name = "contacts"

    filterset_class = FilterContacts




##1/9/2022
from django.forms import modelformset_factory
from .models import ContactImage
from .forms import UploadContactForm, ContactImageForm, Company, CompanyForm #1/18/22

def multiple_contact_view(request):
    ImageFormSet = modelformset_factory(ContactImage, form=ContactImageForm, extra=3)
    #CompanyFormSet = modelformset_factory(Company, form=CompanyForm) #1/18/22

    if request.method == "GET":
        #upload_piece_form = UploadPieceForm()
        upload_contact_form = UploadContactForm(
            #initial={

                ##left side
            #    'title':'Add Title',
            #    'description': 'Add Description',
            #    'medium': 'Add Medium',
            #    'subject_matter': 'Add Subject Matter',
            #    'location': 'Add Location',
            #    'date_of_upload': 'mm/dd/yyyy',

                ##right side
            #    'tags': 'Add Tags', #12-27

            #    }
            ) #9/26
        
        formset = ImageFormSet(queryset=ContactImage.objects.none())
        #formset_company = CompanyFormSet(queryset=Company.objects.none()) #1/18/22
        return render(request, 'contacts/upload_contact_working_copy.html', {"upload_contact_form":upload_contact_form, "formset":formset})
        #return render(request, 'pieces/new1_and_pet_test.html', {"upload_piece_form":upload_piece_form, "formset":formset})
    elif request.method == "POST":
        #upload_piece_form = UploadPieceForm(request.POST)
        upload_contact_form = UploadContactForm(request.POST) #9/26
        
        formset = ImageFormSet(request.POST, request.FILES, prefix='images')
        #formset_company = CompanyFormSet(request.POST, request.FILES) #1/18/22

        if upload_contact_form.is_valid() and formset.is_valid() and formset_company.is_valid():
            data_obj = upload_contact_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image'] #
                    new_image = ContactImage.objects.create(image=image, data=data_obj)
                    new_image.save()

            #1/18/22
            #for form in formset_company.cleaned_data:
            #    if form:
                    #company = form['city'] #1/18/22
                    #company = form['city'] #1/18/22
                    #company = form['city'] #1/18/22
                    #new_image = ContactImage.objects.create(image=image, data=data_obj)
                    #new_image.save()
        
            return render(request, 'contacts/upload_contact_working_copy.html',) ##send pics back as context data
            #return render(request, 'pieces/new1_and_pet_test.html') ##send pics back as context data

            #10/30
#            new_images = PieceImage.objects.all()
#            return render(request, 'pieces/new1_and_pet_test.html', {"new_images" : new_images})
    

#def upload_piece_gallery(request, pk):
#    pass


##end of in use##


### test ###



##new contact view
class NewContactloadView(TemplateView):
    form = NewContactUploadForm
    template_name = 'contacts/new_contact_working_copy.html'
    #template_name = 'contacts/new_contact_in_use.html'

    def post(self, request, *args, **kwargs):

        form = NewContactUploadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('contacts:contacts'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



            ### end test ###