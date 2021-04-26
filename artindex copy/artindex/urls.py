"""artindex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include

from pieces.views import *
from pieces.urls import *

from schedule.views import *
from schedule.urls import *

from contacts.views import *
from schedule.urls import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
]

##urlconf for Add_Edit & Pieces
urlpatterns += [
    path('', include('pieces.urls')),
    ]

##urlconf for schedule
urlpatterns += [
    path('', include('schedule.urls')),
]

##urlconf for contacts
urlpatterns += [
    path('', include('contacts.urls')),
]




##static files
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)