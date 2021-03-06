
from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import index
from .views import footer

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('mails/', include('mails.urls') ),
    path('footer/', footer, name='footer')
]
