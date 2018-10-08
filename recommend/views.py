import django_filters
from rest_framework import viewsets, filters

from .models import Account, Alcohol, Question, Option, Answer
from .serializer import AccountSerializer, AlcoholSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AlcoholViewSet(viewsets.ModelViewSet):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
