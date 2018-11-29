from django.conf.urls import include, url
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView
from bartender.jwt import JWTAuthentication

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^mypage/$', AuthInfoGetView.as_view()),
    url(r'^auth_update/$', AuthInfoUpdateView.as_view()),
    url(r'^delete/$', AuthInfoDeleteView.as_view()),
    url(r'^logout/$', JWTAuthentication),
]