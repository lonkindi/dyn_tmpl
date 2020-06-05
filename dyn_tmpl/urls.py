"""dyn_tmpl URL Configuration

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
from django.contrib import admin
from django.urls import path

from task1.views import inflation_view
from task2.views import home_view, about_view, contacts_view, examples_view

urlpatterns = [
    path('task1/', inflation_view, name='task1'),
    path('task2/', home_view, name='task2'),
    path('task2/about/', about_view, name='about'),
    path('task2/contacts/', contacts_view, name='contacts'),
    path('task2/examples/', examples_view, name='examples'),
    path('admin/', admin.site.urls),
]
