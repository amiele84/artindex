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




                    ### start of in use ### 

#detail list view
class PieceListView(LoginRequiredMixin, FilterView):
    table_class = PiecesTableMedium
    model = NewPiece
    template_name = "pieces/pieces_list_working_copy.html"
    #template_name = "pieces/pieces_list_in_use.html"    #up-to-date
    context_object_name = "pieces"
    ordering = ["price"][0]
   # paginate_by = 5

    filterset_class = FilterTags

    def get_ordering_location(self):
        return self.request.GET.get('sort','price')[-1] #Order live feed events according to closest start date events at the top
        
    

#horizontal list
class PieceListView2(LoginRequiredMixin, FilterView):
    table_class = PiecesTableMedium
    model = NewPiece
    template_name = "pieces/pieces_list2_working_copy.html"
    #template_name = "pieces/pieces_list2_in_use.html"
    context_object_name = "pieces" ##need to change this 

    filterset_class = FilterTags

    def get_ordering_location(self):
        sort = self.request.GET.get('sort','location') #Order live feed events according to closest start date events at the top
        return sort


#big piece pic list
class PieceListView3(LoginRequiredMixin, FilterView):
    table_class = PiecesTableMedium
    model = NewPiece
    template_name = "pieces/pieces_list3_working_copy.html"
    #template_name = "pieces/pieces_list3_in_use.html"
    context_object_name = "pieces" ##need to change this 

    filterset_class = FilterTags

    def get_ordering_location(self):
        sort = self.request.GET.get('sort','location') #Order live feed events according to closest start date events at the top
        return sort


class PieceUpdateView(generic.UpdateView):
    model = NewPiece 
    fields = [
            'artist', 'title',
            'description', 'types', 'medium',
            'subject_matter', 'location', 'date_of_upload',
            'visibility', 'width', 'height', 'depth', 'dim',
            'availability', 'price','tags',
            ]
            
    #template_name_suffix = '_update_form'
    
    template_name = 'pieces/base_pieces_update_form_working_copy.html'
    #template_name = 'pieces/base_pieces_update_form_in_use.html'
    
    success_url = reverse_lazy('artwork:pieces')

#delete piece
class PieceDeleteView(DeleteView):
    model = NewPiece
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('artwork:pieces')





###9/24
#combining new1/ w/ pet
from django.forms import modelformset_factory
from .models import PieceImage
from .forms import UploadPieceForm, PieceImageForm

def multiple_piece_view(request):
    ImageFormSet = modelformset_factory(PieceImage, form=PieceImageForm, extra=3)

    if request.method == "GET":
        #upload_piece_form = UploadPieceForm()
        upload_piece_form = TestForm3(
            initial={

                ##left side
                'title':'Add Title',
                'description': 'Add Description',
                'medium': 'Add Medium',
                'subject_matter': 'Add Subject Matter',
                'location': 'Add Location',
                'date_of_upload': 'mm/dd/yyyy',

                ##right side
                'tags': 'Add Tags', #12-27

                }
            ) #9/26
        
        formset = ImageFormSet(queryset=PieceImage.objects.none())
        return render(request, 'pieces/new1_and_pet_test.html', {"upload_piece_form":upload_piece_form, "formset":formset})
    elif request.method == "POST":
        #upload_piece_form = UploadPieceForm(request.POST)
        upload_piece_form = TestForm3(request.POST) #9/26
        
        formset = ImageFormSet(request.POST, request.FILES)

        if upload_piece_form.is_valid() and formset.is_valid():
            data_obj = upload_piece_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image'] #
                    new_image = PieceImage.objects.create(image=image, data=data_obj)
                    new_image.save()
        
            return render(request, 'pieces/new1_and_pet_test.html') ##send pics back as context data

            #10/30
#            new_images = PieceImage.objects.all()
#            return render(request, 'pieces/new1_and_pet_test.html', {"new_images" : new_images})
    

#def upload_piece_gallery(request, pk):
#    pass





### end of in use ###


#### OUT OF USE ###

##Add_Edit##

##version of this that works 

#uploading images, "Add Piece"
#link in painting list views
# upload/drag image field + submit btn
#creates new Painting Model
class NewPieceUploadView(LoginRequiredMixin, TemplateView):
    
    ##forms
    #form = NewUploadForm #"/new1/"
    #form = PicDataForm #test
    
    ##new1
    template_name = 'pieces/base_pieces_add_piece_working_copy.html'
    #template_name = 'pieces/base_pieces_add_piece_in_use.html'

    ##new2
    #template_name = 'pieces/base_pieces_piece_only_working_copy.html' #new 7-28-21
    #template_name = 'pieces/base_pieces_piece_only_in_use.html' #new 7-28-21

    #template_name = 'pieces/add_piece_in_use.html'
    #template_name = 'pieces/new_upload2_crispy_in_use.html'    #has dropbox

    def post(self, request, *args, **kwargs):

        #new1/
        form = NewUploadForm(request.POST, request.FILES) #"/new1/"
        
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('artwork:piece'))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



                    ##update piece##
#directs from collections url
#just can't change img


#### end of out of use ####




### start of test ###

from django.http import HttpResponse, JsonResponse

class PicOnlyView(TemplateView):
    form = PicOnlyForm

    template_name = 'pieces/base_pieces_piece_only_working_copy.html' #new 7-28-21
    #template_name = 'pieces/base_pieces_piece_only_in_use.html' #new 7-28-21 

def pic_upload_view(request):
    example_form = DataForm()
    
    ##this is what would be modified using 8/18##
   
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        PicOnly.objects.create(upload_pic=my_file)
        return HttpResponse('')

        #return render(request, 'pieces/base_pieces_piece_data_upload_working_copy.html', {'example_form': example_form})
        #return render(request, 'pieces/base_pieces_piece_data_upload_in_use.html', {'example_form': example_form})

                    ## ##    

    return JsonResponse({'post': 'false'})
    
    #9/20: will return pieces page
    #return HttpResponseRedirect(reverse_lazy('artwork:pieces'))


def pic_upload_dta_view(request, pk):
    try:
        p = PicOnly.objects.get(pk=pk)
    except PicOnly.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'pieces/upload.html', {'pk': p})



###8/18
#tutorial: https://engineertodeveloper.com/how-to-build-a-photo-gallery-with-django-part-1/
from django.forms import modelformset_factory
from .models import PicOnly
from .forms import PicOnlyForm, DataForm

def add_pic_only_view(request):
    PicOnlyFormSet = modelformset_factory(PicOnly, form=PicOnlyForm, extra=3)

    if request.method == "GET":
        data_form = DataForm()
        formset = PicOnlyFormSet(queryset=PicOnly.objects.none())
        return render(request, 'pieces/formset_tutorial.html', {"data_form":data_form, "formset":formset})

        #modify this below for dropzone compatibility
    elif request.method == "POST":
        data_form = DataForm(request.POST)
        formset = PicOnlyFormSet(request.POST, request.FILES)

        if data_form.is_valid() and formset.is_valid():
            data_obj = data_form.save()

            for form in formset.cleaned_data:
                if form:
                    upload_pic = form['upload_pic']
                    PicOnly.objects.create(upload_pic=upload_pic, piece=data_obj)
            return HttpResponseRedirect('/')
        else:
            print(data_form.errors, formset.errors) 

###8/19
#tutorial: https://engineertodeveloper.com/build-a-photo-gallery-with-django-part-2/
#photo gallery
def gallery_view1(request, pk):
    data = DataOnly.objects.get(id=pk)
    return render(request, 'pieces/formset_tutorial_gallery.html', {"data":data})
                 

### 8/23
#actual code taken from: https://engineertodeveloper.com/how-to-build-a-photo-gallery-with-django-part-1/
from django.forms import modelformset_factory
from .models import Image
from .forms import ImageForm, PetForm

def add_pet_view(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == "GET":
        pet_form = PetForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'pieces/formset_tutorial.html', {"pet_form":pet_form, "formset":formset})
    elif request.method == "POST":
        pet_form = PetForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if pet_form.is_valid() and formset.is_valid():
            pet_obj = pet_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(image=image, pet=pet_obj)
            
            new_images = Image.objects.all()
            return render(request, 'pieces/formset_tutorial.html', {"pet_form":pet_form, "formset":formset})
        else:
            print(pet_form.errors, formset.errors)
        


def gallery_view2(request, pk):
    pet = Pet.objects.get(id=pk)
    return render(request, 'pieces/formset_tutorial_gallery.html', {"pet":pet})



###8/25
#test upload form
def test_upload_view(request):
    #ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == "GET":
        #test_form = TestForm() #messy test
        #test_form = TestForm2() #less messy test
        test_form = TestForm3(
            initial={

                ##left side
                'title':'Add Title',
                'description': 'Add Description',
                'medium': 'Add Medium',
                'subject_matter': 'Add Subject Matter',
                'location': 'Add Location',
                'date_of_upload': 'mm/dd/yyyy',
                'width': 0,
                'height':0,
                'depth': 0,

                ##right side

                }
            ) #NewFormUpload
        
        #formset = ImageFormSet(queryset=Image.objects.none())
        #return render(request, 'pieces/base_test_upload_form_82521.html', {"test_form":test_form, "formset":formset})
        return render(request, 'pieces/base_test_upload_091921.html', {"test_form":test_form})
    
    elif request.method == "POST":
        #test_form = TestForm(request.POST)
        #test_form2 = TestForm2(request.POST)
        test_form3 = TestForm3(request.POST)

        #formset = ImageFormSet(request.POST, request.FILES)

        #if test_form.is_valid() and formset.is_valid():
        if test_form.is_valid():
            test_obj = test_form.save()

            #for form in formset.cleaned_data:
            #    if form:
            #        image = form['image']
            #        Image.objects.create(image=image, pet=test_obj)
            return HttpResponseRedirect('/')
        else:
            #print(test_form.errors, formset.errors)
            print(test_form.errors)


##10/11##
#from: 
#from: https://www.geeksforgeeks.org/update-view-function-based-views-django/
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
 
# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
          
    return render(request, "pieces/test_detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id) #gets form
    
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/test/"+id+"/update/") #sync w/ form action=""
 
    # add form dictionary to context
    context["form"] = form

    # add upload object to context
    context['obj'] = obj #10/14
 
    return render(request, "pieces/test_update_view.html", context)



##10/26##
# uploadmultiple pics view
def multiple_piece_view2(request):
    ImageFormSet = modelformset_factory(PieceImage2, form=PieceImageForm2, extra=3)

    if request.method == "GET":
        #upload_piece_form = UploadPieceForm()
        upload_piece_form = TestForm4(
            initial={

                ##left side
                'title':'Add Title',
                'description': 'Add Description',
                'medium': 'Add Medium',
                'subject_matter': 'Add Subject Matter',
                'location': 'Add Location',
                'date_of_upload': 'mm/dd/yyyy',
                'width': 0,
                'height':0,
                'depth': 0,

                ##right side

                }
            ) #9/26
        
        formset = ImageFormSet(queryset=PieceImage2.objects.none())
        return render(request, 'pieces/new1_and_pet_test.html', {"upload_piece_form":upload_piece_form, "formset":formset})
    elif request.method == "POST":
        #upload_piece_form = UploadPieceForm(request.POST)
        upload_piece_form = TestForm4(request.POST) #9/26
        
        formset = ImageFormSet(request.POST, request.FILES)

        if upload_piece_form.is_valid() and formset.is_valid():
            data_obj = upload_piece_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    PieceImage2.objects.create(image=image, data=data_obj)
            return render(request, "/") ##add redirect to upload page, w/ image displaayed



### end of test ###










#Detail:
#single column 
class PieceDetailView(generic.DetailView):
    model = NewPiece
    template_name = 'pieces/piece_detail_working_copy.html'
    context_object_name = 'piece'




        



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



