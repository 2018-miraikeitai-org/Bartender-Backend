# coding: utf-8

from rest_framework import routers
from .views import AccountViewSet, AlcoholViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet


router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'alcohol', AlcoholViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'answer', AnswerViewSet)
