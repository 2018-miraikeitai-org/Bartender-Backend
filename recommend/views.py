#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from .models import Alcohol, Question, Option, Answer, History
from .serializer import AlcoholSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, HistorySerializer
import json
import random
from django.http import JsonResponse
import pandas
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# import MeCab
from collections import OrderedDict
import requests
from datetime import date, datetime
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView


class FirstQuestionView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def get(self, request):
        q = Question.objects.filter(ques_id=1)
        q_json = json.dumps([x.to_dict() for x in q], ensure_ascii=False)
        q_list = json.loads(q_json, object_pairs_hook=OrderedDict)

        o = Option.objects.filter(ques_id=1)
        o_json = json.dumps([x.to_dict() for x in o], ensure_ascii=False)
        o_list = json.loads(o_json, object_pairs_hook=OrderedDict)

        if request.META.get('HTTP_PLATFORM', None) == 'iOS':
            q_list.extend(o_list)
            res = q_list

            return Response(res)
        else:
            res = OrderedDict()
            res.update({"question1": q_list[0]})
            res.update({"option1": o_list[0]})

            return JsonResponse(res)


class QuestionView(APIView):

    @action(detail=False, methods=['post'])
    def post(self, request):
        first_ans = request.data['ans']

        if first_ans == '1':
            q1 = Question.objects.filter(ques_id=2)
            q1_json = json.dumps([x.to_dict() for x in q1], ensure_ascii=False)
            q1_list = json.loads(q1_json, object_pairs_hook=OrderedDict)

            o1 = Option.objects.filter(option_id=first_ans)
            o1_json = json.dumps([x.to_dict() for x in o1], ensure_ascii=False)
            o1_list = json.loads(o1_json, object_pairs_hook=OrderedDict)

            q2 = Question.objects.filter(ques_id=3)
            q2_json = json.dumps([x.to_dict() for x in q2], ensure_ascii=False)
            q2_list = json.loads(q2_json, object_pairs_hook=OrderedDict)

            o2 = Option.objects.filter(option_id=6)
            o2_json = json.dumps([x.to_dict() for x in o2], ensure_ascii=False)
            o2_list = json.loads(o2_json, object_pairs_hook=OrderedDict)

            q3 = Question.objects.filter(ques_id=4)
            q3_json = json.dumps([x.to_dict() for x in q3], ensure_ascii=False)
            q3_list = json.loads(q3_json, object_pairs_hook=OrderedDict)

            o3 = Option.objects.filter(option_id=8)
            o3_json = json.dumps([x.to_dict() for x in o3], ensure_ascii=False)
            o3_list = json.loads(o3_json, object_pairs_hook=OrderedDict)
        elif first_ans == '2':
            q1 = Question.objects.filter(ques_id=2)
            q1_json = json.dumps([x.to_dict() for x in q1], ensure_ascii=False)
            q1_list = json.loads(q1_json, object_pairs_hook=OrderedDict)

            o1 = Option.objects.filter(option_id=first_ans)
            o1_json = json.dumps([x.to_dict() for x in o1], ensure_ascii=False)
            o1_list = json.loads(o1_json, object_pairs_hook=OrderedDict)

            q2 = Question.objects.filter(ques_id=3)
            q2_json = json.dumps([x.to_dict() for x in q2], ensure_ascii=False)
            q2_list = json.loads(q2_json, object_pairs_hook=OrderedDict)

            o2 = Option.objects.filter(option_id=6)
            o2_json = json.dumps([x.to_dict() for x in o2], ensure_ascii=False)
            o2_list = json.loads(o2_json, object_pairs_hook=OrderedDict)

            q3 = Question.objects.filter(ques_id=4)
            q3_json = json.dumps([x.to_dict() for x in q3], ensure_ascii=False)
            q3_list = json.loads(q3_json, object_pairs_hook=OrderedDict)

            o3 = Option.objects.filter(option_id=8)
            o3_json = json.dumps([x.to_dict() for x in o3], ensure_ascii=False)
            o3_list = json.loads(o3_json, object_pairs_hook=OrderedDict)
        elif first_ans == '3':
            q1 = Question.objects.filter(ques_id=2)
            q1_json = json.dumps([x.to_dict() for x in q1], ensure_ascii=False)
            q1_list = json.loads(q1_json, object_pairs_hook=OrderedDict)

            o1 = Option.objects.filter(option_id=first_ans)
            o1_json = json.dumps([x.to_dict() for x in o1], ensure_ascii=False)
            o1_list = json.loads(o1_json, object_pairs_hook=OrderedDict)

            q2 = Question.objects.filter(ques_id=3)
            q2_json = json.dumps([x.to_dict() for x in q2], ensure_ascii=False)
            q2_list = json.loads(q2_json, object_pairs_hook=OrderedDict)

            o2 = Option.objects.filter(option_id=7)
            o2_json = json.dumps([x.to_dict() for x in o2], ensure_ascii=False)
            o2_list = json.loads(o2_json, object_pairs_hook=OrderedDict)

            q3 = Question.objects.filter(ques_id=5)
            q3_json = json.dumps([x.to_dict() for x in q3], ensure_ascii=False)
            q3_list = json.loads(q3_json, object_pairs_hook=OrderedDict)

            o3 = Option.objects.filter(option_id=9)
            o3_json = json.dumps([x.to_dict() for x in o3], ensure_ascii=False)
            o3_list = json.loads(o3_json, object_pairs_hook=OrderedDict)
        elif first_ans == '4':
            q1 = Question.objects.filter(ques_id=2)
            q1_json = json.dumps([x.to_dict() for x in q1], ensure_ascii=False)
            q1_list = json.loads(q1_json, object_pairs_hook=OrderedDict)

            o1 = Option.objects.filter(option_id=first_ans)
            o1_json = json.dumps([x.to_dict() for x in o1], ensure_ascii=False)
            o1_list = json.loads(o1_json, object_pairs_hook=OrderedDict)

            q2 = Question.objects.filter(ques_id=3)
            q2_json = json.dumps([x.to_dict() for x in q2], ensure_ascii=False)
            q2_list = json.loads(q2_json, object_pairs_hook=OrderedDict)

            o2 = Option.objects.filter(option_id=7)
            o2_json = json.dumps([x.to_dict() for x in o2], ensure_ascii=False)
            o2_list = json.loads(o2_json, object_pairs_hook=OrderedDict)

            q3 = Question.objects.filter(ques_id=4)
            q3_json = json.dumps([x.to_dict() for x in q3], ensure_ascii=False)
            q3_list = json.loads(q3_json, object_pairs_hook=OrderedDict)

            o3 = Option.objects.filter(option_id=8)
            o3_json = json.dumps([x.to_dict() for x in o3], ensure_ascii=False)
            o3_list = json.loads(o3_json, object_pairs_hook=OrderedDict)

        if request.META.get('HTTP_PLATFORM', None) == 'iOS':
            q1_list.extend(o1_list)
            q1_list.extend(q2_list)
            q1_list.extend(o2_list)
            q1_list.extend(q3_list)
            q1_list.extend(o3_list)
            res = q1_list

            return Response(res)
        else:
            res = OrderedDict()
            res.update({"question2": q1_list[0]})
            res.update({"option2": o1_list[0]})
            res.update({"question3": q2_list[0]})
            res.update({"option3": o2_list[0]})
            res.update({"question4": q3_list[0]})
            res.update({"option4": o3_list[0]})

            return JsonResponse(res)


def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError("Type %s not serializable" % type(obj))


class HistoryView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['post'])
    def post(self, request):  # 受けとったデータを履歴テーブルに追加する
        hc = History.objects.count()
        h = History(
            history_id=hc + 1,
            user_id=request.user.user_id,
            alco_name=request.data['alco_name'],
            data_joined=timezone.now()
        )
        h.save()

        return Response(data={
            "message": "履歴に保存しました"
        },
            status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def get(self, request):     # 履歴データを渡す
        try:
            sh = History.objects.filter(user_id=request.user.user_id)
            sh_json = json.dumps([x.to_dict() for x in sh], default=json_serial, ensure_ascii=False)
            sh_list = json.loads(sh_json, object_pairs_hook=OrderedDict)

            if request.META.get('HTTP_PLATFORM', None) == 'iOS':
                for i in range(sh.count()):
                    alcohol = Alcohol.objects.get(alco_name=sh_list[i]['alco_name'])
                    sh_list[i].update({"image": alcohol.image, "detail": alcohol.detail})

                sh_list.reverse()  # 降順に並び替え

                return Response(sh_list)
            else:
                res = OrderedDict()

                for i in range(sh.count())[::-1]:  # 降順に並び替え[::-1]
                    alcohol = Alcohol.objects.get(alco_name=sh_list[i]['alco_name'])
                    sh_list[i].update({"image": alcohol.image, "detail": alcohol.detail})
                    res.update({"history" + str(sh.count() - i): sh_list[i]})

                return JsonResponse(res)
        except History.DoesNotExist:
            return Response(data={
                "message": "History matching query does not exist"
            },
                status=status.HTTP_400_BAD_REQUEST)


class ReviewView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['post'])
    def post(self, request):  # reviewデータを渡す
        try:
            user_id = request.user.user_id
            history = History.objects.get(user_id=user_id, alco_name=request.data['alco_name'])

            return Response(data={
                'history_id': history.history_id,
                'user_id': history.user_id,
                'alco_name': history.alco_name,
                'data_joined': history.data_joined,
                'review': history.review
            })
        except History.DoesNotExist:
            return Response(data={
                "message": "History matching query does not exist"
            },
                status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def put(self, request):  # 受けとったデータを履歴テーブルのreviewに追加する
        try:
            user_id = request.user.user_id
            review = request.data['review']

            history = History.objects.get(user_id=user_id, alco_name=request.data['alco_name'])
            history.review = review
            history.save()

            return Response(data={
                "message": "レビューを更新しました"
            },
                status=status.HTTP_200_OK)
        except History.DoesNotExist:
            return Response(data={
                "message": "History matching query does not exist"
            },
                status=status.HTTP_400_BAD_REQUEST)

"""
class WordDividor:
    INDEX_CATEGORY = 0
    INDEX_ROOT_FORM = 6
    TARGET_CATEGORIES = ["名詞"]

    def __init__(self, dictionary="mecabrc"):
        self.dictionary = dictionary
        self.tagger = MeCab.Tagger(self.dictionary)

    def extract_words(self, text):
        if not text:
            return []

        words = []

        self.tagger.parse('')
        node = self.tagger.parseToNode(text)
        while node:
            features = node.feature.split(',')

            if features[self.INDEX_CATEGORY] in self.TARGET_CATEGORIES:
                if features[self.INDEX_ROOT_FORM] == "*":
                    words.append(node.surface)
                else:
                    # prefer root form
                    words.append(features[self.INDEX_ROOT_FORM])

            node = node.next

        return words
"""


class RecommendView(APIView):

    @action(detail=False, methods=['post'])
    def post(self, request):
        ans = request.data['ans']

        r = Alcohol.objects.filter(type_name__contains=ans)
        if r.count() > 1:
            res_json = json.dumps([x.to_dict() for x in r], ensure_ascii=False)
            res = json.loads(res_json, object_pairs_hook=OrderedDict)
            #  = json.dumps(res[random.randrange(r.count())], ensure_ascii=False)
            ans_id = res[random.randrange(r.count())]['alcohol_id']  # 回答結果のalcohol_id
        else:
            res_json = json.dumps([x.to_dict() for x in r], ensure_ascii=False)
            res = json.loads(res_json, object_pairs_hook=OrderedDict)
            ans_id = res[0]['alcohol_id']  # 回答結果のalcohol_id


        '''
        dataset = pandas.read_csv("recommend/cocktail_data.csv")
        docs = numpy.array(dataset["detail"])

        def vecs_array(docs):
            wd = WordDividor()
            vectorizer = TfidfVectorizer(
                analyzer=wd.extract_words
            )
            vecs = vectorizer.fit_transform(docs.astype('U'))
            return vecs.toarray()

        cs_array = cosine_similarity(vecs_array(docs), vecs_array(docs))
        cocktail = cs_array[ans_id - 1].argsort()[::-1][:3]
        '''

        cs = Answer.objects.filter(alcohol_id=ans_id)
        cs_json = json.dumps([x.to_dict() for x in cs], ensure_ascii=False)
        cs_res = json.loads(cs_json, object_pairs_hook=OrderedDict)
        cs_list = numpy.array(cs_res[0]['learning_data'])
        cocktail = cs_list.argsort()[::-1][:3]

        if request.META.get('HTTP_PLATFORM', None) == 'iOS':
            res = []
            for i in range(len(cocktail)):
                r = Alcohol.objects.filter(alcohol_id=cocktail[i] + 1)
                ans_json = json.dumps([x.to_dict() for x in r], ensure_ascii=False)
                ans_list = json.loads(ans_json, object_pairs_hook=OrderedDict)
                res.extend(ans_list)

            return Response(res)
        else:
            res = OrderedDict()
            for i in range(len(cocktail)):
                r = Alcohol.objects.filter(alcohol_id=cocktail[i] + 1)
                ans_json = json.dumps([x.to_dict() for x in r], ensure_ascii=False)
                ans_list = json.loads(ans_json, object_pairs_hook=OrderedDict)
                res.update({"answer" + str(i + 1): ans_list[0]})

            return JsonResponse(res)


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


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
