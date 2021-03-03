from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Mail
# Create your views here.
class MailListView(ListView):
    model = Mail
    template_name = 'mails/list.html'
    paginate_by = 10

class MailCreateView(CreateView):
    model = Mail
    template_name = 'mails/create.html'
    form_class