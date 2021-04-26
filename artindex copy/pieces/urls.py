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
