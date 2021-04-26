from django.urls import path, include

from .views import *

app_name = 'artwork'

urlpatterns = [
    path('pieces/', PieceListView.as_view(), name='pieces'),
    path('pieces/new/', NewPieceUploadView.as_view(), name='new-upload'),
    path('pieces/<uuid:pk>/', PieceDetailView.as_view(), name="detail"),
    path('pieces/<uuid:pk>/update/', PieceUpdateView.as_view(), name='piece-update'),
    path('pieces/<uuid:pk>/delete/', PieceDeleteView.as_view(), name='delete'),
]

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