from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect

from django.conf import settings

from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

from .models import Mail
from users.models import User
from user_mails.models import UserMail

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

class MailDetailView(DetailView):
    model = Mail
    template_name = 'mails/detail.html'

def create_mail(subject, user, template_path='', context={}):
    template = get_template(template_path)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject,
        'Fernando',
        settings.EMAIL_HOST_USER,
        [user.email]
    )

    message.attach_alternative(content, 'text/html')
    return message


def send(request, pk):
    mail = get_object_or_404(Mail, pk=pk)
    # generamos una instancia de PasswordResetTokenGenerator
    token_generator = PasswordResetTokenGenerator()
    # for user in User.objects.filter(newsletter=True):
    # Left join
    # excluir a todos los usuarios a los que se han enviaod el mail
    for user in User.objects.exclude(usermail__mail=mail).filter(newsletter=True):
        token = token_generator.make_token(user)
        user_mail = UserMail.objects.create(user=user, mail=mail, token=token)

        context = {'mail':mail, 'user':user, 'token':token}
        email = create_mail(mail.subject, user, 'mails/base/base.html', context)
        email.send(fail_silently=False)

        user_mail.sent_at = timezone.now()
        user_mail.save()
    return redirect('mails:detail', mail.id)