#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from rest_framework import routers
from .views import AlcoholViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet, HistoryViewSet
from .views import FirstQuestionView, QuestionView, RecommendView
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
# router.register(r'account', AccountViewSet)
router.register(r'alcohol', AlcoholViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
    url(r'alcohol/', RecommendView.as_view()),
    url(r'question/first', FirstQuestionView.as_view()),
    url(r'question/', QuestionView.as_view()),

]
