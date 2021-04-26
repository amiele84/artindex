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
    template_name = 'pieces/new_upload2_crispy_working_copy.html'
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



