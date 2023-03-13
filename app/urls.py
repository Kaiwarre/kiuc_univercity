from .views import *
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name='home'),
    path('education/<int:pk>', edu_detail, name='edu_detail'),
    path('page/<int:pk>', page_detail, name='page_detail'),
    path('teachers/<int:pk>', teachers_list, name='teachers'),
    path('courses/<int:pk>', courses_list, name='courses'),
]