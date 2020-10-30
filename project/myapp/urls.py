"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_settings', views.admin_settings, name='admin_settings'),
    path('admin_settings_404', views.admin_settings_404, name='admin_settings_404'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_settings', views.user_settings, name='user_settings'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_query_add', views.user_query_add, name='user_query_add'),
    path('user_query_delete', views.user_query_delete, name='user_query_delete'),
    path('user_query_view', views.user_query_view, name='user_query_view'),
]
