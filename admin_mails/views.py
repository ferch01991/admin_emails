from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def footer(request):
    print('\nSe realizo una peticion')
    with open(settings.IMAGE_DIR / 'footer_python.png', 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')