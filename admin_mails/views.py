from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from user_mails.models import UserMail

def index(request):
    return render(request, 'index.html', {})

def footer(request):
    print('--------------------------------------')
    print(request.GET.get('token'))
    if request.GET.get('token'):
        user_mail = UserMail.objects.filter(token=request.GET['token']).first()
        print(user_mail)

        if user_mail:
            user_mail.update_read()

    print('\nSe realizo una peticion')
    with open(settings.IMAGE_DIR / 'footer_python.png', 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')