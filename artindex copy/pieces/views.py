from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django_tables2 import SingleTableView

from django.utils.decorators import method_decorator


from .forms import *
from .tables import *
from .filters import *
from .models import *

# Create your views here.

##sidebar
def index(request):
    return render(request, 'index.html')


                ## pieces ##

##3 types of views for pieces lists

#Large:title, img large thumbnail w/ 3x3
class PiecesListLargeView(SingleTableView, FilterView):
    pass

#Medium:
#single col
class PieceListView(SingleTableMixin, FilterView):
    table_class = PiecesTableMedium
    model = NewPiece
    template_name = "pieces/pieces2.html"
    context_object_name = "pieces"
   # paginate_by = 5

    filterset_class = AvailabilityFilter

#class FilteredPieceListView2(SingleTableMixin, FilterView):
#    table_class = PiecesTableMedium
#    model = NewPiece
#    template_name = "pieces/pieces.html"

    #filterset_class = AvailabilityFilter

#Detail:
#single column 
class PieceDetailView(generic.DetailView):
    model = NewPiece
    template_name = 'pieces/piece_detail.html'


#update piece
#directs from collections url
#just can't change img
class PieceUpdateView(generic.UpdateView):
    model = NewPiece 
    fields = ["title", "artist"]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('artwork:pieces')

#delete piece
class PieceDeleteView(DeleteView):
    model = NewPiece
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('artwork:pieces')



                    ##Add_Edit##

#uploading images, "Add Piece"
#link in painting list views
# upload/drag image field + submit btn
#creates new Painting Model
class NewPieceUploadView(TemplateView):
    form = NewUploadForm
    template_name = 'pieces/new_upload.html'

    def post(self, request, *args, **kwargs):

        form = NewUploadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('artwork:pieces'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)





                    ##New Artist##

#create new artist model
class NewArtistCreateView(CreateView):
    form = NewArtistCreateForm
    template_name = 'pieces/new_artist_create.html'

    def post(self, request, *args, **kwargs):

        form = NewArtistCreateForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('artwork:pieces'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



