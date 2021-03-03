from django.urls import path
from .views import MailListView
from .views import MailCreateView

app_name = 'mails'

urlpatterns = [
    path('', MailListView.as_view(), name='list'), #convertir una clase a una vista
    path('create', MailCreateView.as_view(), name='create'),
]
