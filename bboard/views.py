from django.shortcuts import render
from django.http import HttpResponse
from .models import Bd


# Create your views here.
def index(request):
    s = 'Список объявлений \r\n\r\n\r\n'
    for b in Bd.objects.order_by('-published'):
        s += f'{b.title} \r\n {b.content} \r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
