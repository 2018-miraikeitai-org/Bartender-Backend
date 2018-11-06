#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""bartender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from recommend.urls import router as recommend_router
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api2/', include(recommend_router.urls)),
    url(r'api/', include('recommend.urls')),
    url(r'^user/login/', obtain_jwt_token),
    url(r'user/', include('accounts.urls')),
]
