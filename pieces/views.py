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


##in use 

#Medium:
#single col
class PieceListView(LoginRequiredMixin, FilterView):
    table_class = PiecesTableMedium
    model = NewPiece
    template_name = "pieces/pieces_list_working_copy.html"
    #template_name = "pieces/pieces_try_in_use.html"    #up-to-date
    context_object_name = "pieces"
#    ordering = ["location"]
   # paginate_by = 5

    filterset_class = FilterTags

    def get_ordering_location(self):
        sort = self.request.GET.get('sort','location') #Order live feed events according to closest start date events at the top
        return sort
    

#class FilteredPieceListView2(SingleTableMixin, FilterView):
#    table_class = PiecesTableMedium
#    model = NewPiece
#    template_name = "pieces/pieces.html"

    #filterset_class = AvailabilityFilter

#Detail:
#single column 
class PieceDetailView(generic.DetailView):
    model = NewPiece
    template_name = 'pieces/piece_detail_working_copy.html'
    context_object_name = 'piece'


#update piece
#directs from collections url
#just can't change img
class PieceUpdateView(generic.UpdateView):
    model = NewPiece 
    fields = [
            'artist', 'title',
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price','tags',
            ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('artwork:pieces')

#delete piece
class PieceDeleteView(DeleteView):
    model = NewPiece
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('artwork:pieces')



                    ##Add_Edit##


##version of this that works 

#uploading images, "Add Piece"
#link in painting list views
# upload/drag image field + submit btn
#creates new Painting Model
class NewPieceUploadView(LoginRequiredMixin, TemplateView):
    form = NewUploadForm
    template_name = 'pieces/add_piece_working_copy.html'
    #template_name = 'pieces/new_upload2_crispy_in_use.html'    #has dropbox

    def post(self, request, *args, **kwargs):

        form = NewUploadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('artwork:pieces'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        



##collections
class CollectionsListView(LoginRequiredMixin, generic.ListView):
    model = NewPiece
    queryset = NewPiece.objects.filter(location='NYC')
    template_name ='pieces/collections_working_copy.html'
    #paginate_by = 10
    context_object_name = 'collections'

    filterset = CollectionFilter

#    def get_queryset(self):
#        collection = NewPiece.objects.filter(uploader_id=self.request.user).values()
#        return render( 'pieces/collections_working_copy.html', {'collection': collection})
#        return NewPiece.objects.filter(uploader=self.request.user)



##end of in use##



##piece dropzone page
class PieceOnlyUploadView(TemplateView):
    form = PieceUploadOnlyForm
    template_name= 'pieces/piece_only_upload_in_use.html'
    #template_name= 'pieces/piece_only_upload_working_copy.html'    #not in use
    success_url = reverse_lazy('artwork:pieces')









##piece dropzone page2
#adapted from: https://www.existenceundefined.com/blog/programming/13/django-multiple-image-upload-with-dropzonejs
class PieceOnlyUploadView2(TemplateView):
    template_name = 'pieces/piece_only_upload2.html' 

    def post(self, request):
        body = request.POST.get('body', "")
        images = request.FILES.get('file[0]', None)

        if body or images:
            author = request.user
            post = SocialMediaPost()
            post.body = body
            post.author = author
            post.datetime_created = timezone.now()
            post.save()

            files = [request.FILES.get('file[%d]' % i) for i in range(0, len(request.FILES))]

            for image in files:
                photo = Photo(photo=image, user=request.user, obj_type='post', obj_id=post.pk)
                photo.save()

        return JsonResponse({'message': 'Post created'}, status=200)









##test
class NewPieceUploadView_1(TemplateView):
    form = ContactForm
    template_name = 'pieces/tutorial.html'

    def post(self, request, *args, **kwargs):

        form = ContactForm_Tutorial(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('artwork:tutorial-upload'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


##test
class TutorialListView(SingleTableMixin, FilterView):
    #table_class = PiecesTableMedium
    model = NewPiece_1
    template_name = "pieces/tutorial_list.html"
    context_object_name = "tutorials"


##test: https://www.geeksforgeeks.org/render-django-form-fields-manually/
def home_view(request): 
    context ={} 
    context['form']= InputForm() 
    return render(request, "pieces/home.html", context) 



