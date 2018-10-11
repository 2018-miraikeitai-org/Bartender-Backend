from rest_framework import viewsets
from .models import Account, Alcohol, Question, Option, Answer
from .serializer import AccountSerializer, AlcoholSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer
import json
import random
from django.core import serializers
from django.http import HttpResponse
# from django.http import JsonResponse


def first_question(request):
    q = Question.objects.filter(ques_id=1)
    q_json = serializers.serialize("json", q, ensure_ascii=False)
    q_list = json.loads(q_json)

    o = Option.objects.filter(ques_id=1)
    o_json = serializers.serialize("json", o, ensure_ascii=False)
    o_list = json.loads(o_json)

    q_list.extend(o_list)
    res_json = json.dumps(q_list, ensure_ascii=False, indent=4, separators=(',', ': '))
    # return res_json
    return HttpResponse(res_json)


def question(request):
    if request.method == 'GET':
        first_ans = request.GET.get("ans")
    elif request.method == 'POST':
        first_ans = request.POST.get("ans")

    if first_ans == '1':
        q1 = Question.objects.filter(ques_id=2)
        q1_json = serializers.serialize("json", q1, ensure_ascii=False)
        q1_list = json.loads(q1_json)

        o1 = Option.objects.filter(option_id=first_ans)
        o1_json = serializers.serialize("json", o1, ensure_ascii=False)
        o1_list = json.loads(o1_json)

        q2 = Question.objects.filter(ques_id=3)
        q2_json = serializers.serialize("json", q2, ensure_ascii=False)
        q2_list = json.loads(q2_json)

        o2 = Option.objects.filter(option_id=6)
        o2_json = serializers.serialize("json", o2, ensure_ascii=False)
        o2_list = json.loads(o2_json)

        q3 = Question.objects.filter(ques_id=4)
        q3_json = serializers.serialize("json", q3, ensure_ascii=False)
        q3_list = json.loads(q3_json)

        o3 = Option.objects.filter(option_id=8)
        o3_json = serializers.serialize("json", o3, ensure_ascii=False)
        o3_list = json.loads(o3_json)
    elif first_ans == '2':
        q1 = Question.objects.filter(ques_id=2)
        q1_json = serializers.serialize("json", q1, ensure_ascii=False)
        q1_list = json.loads(q1_json)

        o1 = Option.objects.filter(option_id=first_ans)
        o1_json = serializers.serialize("json", o1, ensure_ascii=False)
        o1_list = json.loads(o1_json)

        q2 = Question.objects.filter(ques_id=3)
        q2_json = serializers.serialize("json", q2, ensure_ascii=False)
        q2_list = json.loads(q2_json)

        o2 = Option.objects.filter(option_id=6)
        o2_json = serializers.serialize("json", o2, ensure_ascii=False)
        o2_list = json.loads(o2_json)

        q3 = Question.objects.filter(ques_id=4)
        q3_json = serializers.serialize("json", q3, ensure_ascii=False)
        q3_list = json.loads(q3_json)

        o3 = Option.objects.filter(option_id=8)
        o3_json = serializers.serialize("json", o3, ensure_ascii=False)
        o3_list = json.loads(o3_json)
    elif first_ans == '3':
        q1 = Question.objects.filter(ques_id=2)
        q1_json = serializers.serialize("json", q1, ensure_ascii=False)
        q1_list = json.loads(q1_json)

        o1 = Option.objects.filter(option_id=first_ans)
        o1_json = serializers.serialize("json", o1, ensure_ascii=False)
        o1_list = json.loads(o1_json)

        q2 = Question.objects.filter(ques_id=3)
        q2_json = serializers.serialize("json", q2, ensure_ascii=False)
        q2_list = json.loads(q2_json)

        o2 = Option.objects.filter(option_id=7)
        o2_json = serializers.serialize("json", o2, ensure_ascii=False)
        o2_list = json.loads(o2_json)

        q3 = Question.objects.filter(ques_id=5)
        q3_json = serializers.serialize("json", q3, ensure_ascii=False)
        q3_list = json.loads(q3_json)

        o3 = Option.objects.filter(option_id=9)
        o3_json = serializers.serialize("json", o3, ensure_ascii=False)
        o3_list = json.loads(o3_json)
    elif first_ans == '4':
        q1 = Question.objects.filter(ques_id=2)
        q1_json = serializers.serialize("json", q1, ensure_ascii=False)
        q1_list = json.loads(q1_json)

        o1 = Option.objects.filter(option_id=first_ans)
        o1_json = serializers.serialize("json", o1, ensure_ascii=False)
        o1_list = json.loads(o1_json)

        q2 = Question.objects.filter(ques_id=3)
        q2_json = serializers.serialize("json", q2, ensure_ascii=False)
        q2_list = json.loads(q2_json)

        o2 = Option.objects.filter(option_id=7)
        o2_json = serializers.serialize("json", o2, ensure_ascii=False)
        o2_list = json.loads(o2_json)

        q3 = Question.objects.filter(ques_id=4)
        q3_json = serializers.serialize("json", q3, ensure_ascii=False)
        q3_list = json.loads(q3_json)

        o3 = Option.objects.filter(option_id=8)
        o3_json = serializers.serialize("json", o3, ensure_ascii=False)
        o3_list = json.loads(o3_json)

    # elseにエラーを返す処理書きたい

    q1_list.extend(o1_list)
    q1_list.extend(q2_list)
    q1_list.extend(o2_list)
    q1_list.extend(q3_list)
    q1_list.extend(o3_list)
    res_json = json.dumps(q1_list, ensure_ascii=False)
    # return res_json
    return HttpResponse(res_json)


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
