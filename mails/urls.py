from django.urls import path
from .views import MailListView
from .views import MailCreateView
from .views import MailDeleteView
from .views import MailUpdateView
from .views import MailDetailView

app_name = 'mails'

urlpatterns = [
    path('', MailListView.as_view(), name='list'), #convertir una clase a una vista
    path('create', MailCreateView.as_view(), name='create'),
    path('detail/<int:pk>', MailDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MailUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MailDeleteView.as_view(), name='delete'),
]
