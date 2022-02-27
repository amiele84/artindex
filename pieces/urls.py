from django.urls import path, include

from .views import *

app_name = 'artwork'


                    ### in use ###

urlpatterns = [
    path('pieces/', PieceListView.as_view(), name='pieces'),
    path('pieces2/', PieceListView2.as_view(), name='pieces2'),
    path('pieces3/', PieceListView3.as_view(), name='pieces3'),
    path('pieces/new1/', NewPieceUploadView.as_view(), name='new-upload1'), #test below
    path('pieces/<uuid:pk>/', PieceDetailView.as_view(), name="detail"),
    path('pieces/<uuid:pk>/update/', PieceUpdateView.as_view(), name='piece-update'),
    path('pieces/<uuid:pk>/delete/', PieceDeleteView.as_view(), name='delete'),
]

                    ### end of in use ###






                    ### start of test ###
###8/8
#for dropbox 
urlpatterns += [
    path('pieces/new2/', PicOnlyView.as_view(), name='new-upload2'),
    path('pieces/new2/upload/', pic_upload_view, name='upload-view'),
    #path('pieces/new/upload/', pic_upload_dta_view, name='upload-view'), #not working
 ]


###8/18
#tutorial: https://engineertodeveloper.com/how-to-build-a-photo-gallery-with-django-part-1/
#not working properly
from .views import add_pic_only_view

urlpatterns += [
    path('pieces/new3/', add_pic_only_view, name='new-upload3'),
    path('pieces/new3/<int:pk>/', gallery_view1, name="pieces-index") #8/19
]


### 8/23
#actual code from:
from .views import add_pet_view

urlpatterns += [
    path('pet/', add_pet_view, name="pet_index"),
    path('pet/<int:pk>/', gallery_view2, name="pet_index"),
]


###8/25
#test upload
from .views import test_upload_view

urlpatterns += [
    path('pieces/test/upload/', test_upload_view, name='test-upload'),
]


###9/24
#combining new1/ w/ pet
from .views import multiple_piece_view, multiple_piece_view2

urlpatterns += [
    path('pieces/uploadpiece/', multiple_piece_view, name="upload_piece_index"), #10/28
    #path('pieces/uploadpiece/<int:pk>/', upload_piece_gallery, name="upload_piece_index"),
]

##10/11
from .views import update_view, detail_view
 
urlpatterns += [
    path('test/<id>/', detail_view ),
    path('test/<id>/update/', update_view ),
]
 
##10/13
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 
                    ### end of test ###








#urlpatterns += [
#    path('tutorial/', TutorialListView.as_view(), name='tutorial'),
#    path('tutorial/new/', NewPieceUploadView.as_view(), name='tutorial-upload')
#]

##test: https://www.geeksforgeeks.org/render-django-form-fields-manually/
urlpatterns += [
    path('home/', home_view, name="home"),
]

##upload dropzone
urlpatterns += [
    path('pieces/upload/', PieceOnlyUploadView.as_view(), name='piece-only'),
    path('pieces/upload-2/', PieceOnlyUploadView2.as_view(), name="piece-only-2"),
]

##collections
urlpatterns += [
    path('pieces/collection/', CollectionsListView.as_view(), name='my-collection'),
]