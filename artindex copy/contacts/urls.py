from django.urls import path, include

from .views import *

app_name = 'contacts'

urlpatterns = [
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('contacts/new/', NewContactloadView.as_view(), name='new-contact'),
    path('contacts/<uuid:pk>/', ContactsDetailView.as_view(), name='detail'),
    path('contacts/<uuid:pk>/update', ContactsUpdateView.as_view(), name='contact-update'),
    path('contacts/<uuid:pk>/delete/', ContactsDeleteView.as_view(), name='delete'),
]