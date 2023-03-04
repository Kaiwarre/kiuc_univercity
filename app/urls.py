from .views import *
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name='home'),
    path('education/<int:pk>', edu_detail, name='edu_detail'),
    path('page/<int:pk>', page_detail, name='page_detail')
    # path('register', register, name='register'),
    # path('login', auth_view.LoginView.as_view(template_name='main/login.html'), name='login'),
    # path('logout', auth_view.LogoutView.as_view(), name='logout'),
    # path('tech', tech, name='tech'),
    # path('category/<int:pk>', humor, name='category'),
    # path('science', science, name='science'),
    # path('nature', nature, name='nature'),
]