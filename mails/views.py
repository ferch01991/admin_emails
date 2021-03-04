from django.shortcuts import render
from django.shortcuts import reverse

from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Mail

from .forms import CreateMailForm

# Create your views here.
class MailListView(ListView):
    model = Mail
    template_name = 'mails/list.html'
    paginate_by = 10

class MailCreateView(CreateView):
    model = Mail
    template_name = 'mails/create.html'
    form_class = CreateMailForm

    def get_success_url(self):
        return reverse('mails:list')

class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mails:list')

class MailUpdateView(UpdateView):
    model = Mail
    form_class = CreateMailForm
    template_name = 'mails/update.html'

    def get_success_url(self):
        return reverse('mails:list')