from django.shortcuts import render
from .models import *


def home(request):
    edus = Education.objects.all()
    page = Page.objects.all()
    return render(request, 'index.html', {'edus': edus, 'page': page})


def edu_detail(request, pk):
    edus = Education.objects.all()
    page = Page.objects.all()
    return render(request, 'edu_detail.html', {'edu': Education.objects.get(id=pk), 'edus': edus, 'page': page})


def page_detail(request, pk):
    edus = Education.objects.all()
    page = Page.objects.all()
    return render(request, 'page_detail.html', {'page': Page.objects.get(id=pk), 'edu': Education.objects.get(id=pk),'edus': edus, 'page': page})