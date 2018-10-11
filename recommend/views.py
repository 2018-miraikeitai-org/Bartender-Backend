from rest_framework import viewsets
from .models import Account, Alcohol, Question, Option, Answer
from .serializer import AccountSerializer, AlcoholSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer
import json
import random
from django.core import serializers
from django.http import HttpResponse
# from django.http import JsonResponse


def recommend(request):
    if request.method == 'GET':
        ans = request.GET.get("ans")
    elif request.method == 'POST':
        ans = request.POST.get("ans")

    r = Alcohol.objects.filter(type_name__contains=ans)
    if r.count() > 1:
        res_json = serializers.serialize("json", r, ensure_ascii=False)
        res = json.loads(res_json)
        res_json = json.dumps(res[random.randrange(r.count())], ensure_ascii=False)
    else:
        res_json = serializers.serialize("json", r, ensure_ascii=False)

    # return res_json
    return HttpResponse(res_json)


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
