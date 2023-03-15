from django.shortcuts import render
from .models import *


def home(request):
    edus = Education.objects.all()
    page = Page.objects.all()
    ads = Ads.objects.all()
    anons = Anons.objects.all()
    return render(request, 'index.html', {'edus': edus, 'page': page, 'ads': ads, 'anons': anons})


def edu_detail(request, pk):
    edus = Education.objects.all()
    page = Page.objects.all()
    return render(request, 'edu_detail.html', {'edu': Education.objects.get(id=pk), 'edus': edus, 'page': page})


def page_detail(request, pk):
    edus = Education.objects.all()
    pages = Page.objects.all()
    page = Page.objects.get(id=pk)
    return render(request, 'page_detail.html', {'page': page, 'edu': page.category, 'edus': edus, 'pages': pages})


def teachers_list(request, pk):
    teachers = Teacher.objects.filter(education=pk)
    edus = Education.objects.all()
    edu = Education.objects.get(id=pk)
    page = Page.objects.all()
    return render(request, 'teacher_list.html', {'edu': edu, 'edus': edus, 'teachers': teachers,'page': page})

def courses_list(request, pk):
    courses = Course.objects.filter(education=pk)
    edus = Education.objects.all()
    edu = Education.objects.get(id=pk)
    page = Page.objects.all()
    return render(request, 'courses_list.html', {'edu': edu, 'edus': edus, 'courses': courses, 'page': page})

def ads_detail(request, pk):
    ads = Ads.objects.get(id=pk)
    edus = Education.objects.all()
    return render(request, 'ads_detail.html', {'ads': ads, 'edus': edus })

def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    edus = Education.objects.all()
    edu = Education.objects.get(id=pk)
    page = Page.objects.all()
    return render(request, 'course_detail.html', {'course': course, 'edu': edu, 'edus': edus, 'page': page })



