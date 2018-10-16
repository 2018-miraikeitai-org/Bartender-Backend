#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from rest_framework import routers
from .views import AccountViewSet, AlcoholViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'alcohol', AlcoholViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'answer', AnswerViewSet)


urlpatterns = [
    url(r'alcohol/', views.recommend, name='recommend'),
    url(r'question/first', views.first_question, name='first_question'),
    url(r'question/', views.question, name='question'),

]
