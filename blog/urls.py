"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='homepage'),
    url(r'^en/$', Home.as_view(), {'lang': 'en'}, name='homgpage_eng'),
    url(r'^(?P<slug>[\w\-]+)/$', ReadPost.as_view(), name='readpost'),
    url(r'^(?P<slug>[\w\-]+)/en$', ReadPost.as_view(), {'lang': 'en'}, name='readpost_eng'),
]
