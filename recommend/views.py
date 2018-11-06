#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from rest_framework import viewsets
from .models import Alcohol, Question, Option, Answer, History
from .serializer import AlcoholSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, HistorySerializer
import json
import random
from django.http import JsonResponse
import pandas
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import MeCab
from collections import OrderedDict
from rest_framework import permissions
from rest_framework.views import APIView


class FirstQuestionView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        q = Question.objects.filter(ques_id=1)
        q_json = json.dumps([x.to_dict() for x in q], ensure_ascii=False)
        q_list = json.loads(q_json, object_pairs_hook=OrderedDict)

        o = Option.objects.filter(ques_id=1)
        o_json = json.dumps([x.to_dict() for x in o], ensure_ascii=False)
        o_list = json.loads(o_json, object_pairs_hook=OrderedDict)

        res = OrderedDict()
        res.update({"question1": q_list[0]})
        res.update({"option1": o_list[0]})

        return JsonResponse(res)


class QuestionView(APIView):

    def post(self, request, format=None):
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

        res = OrderedDict()
        res.update({"question2": q1_list[0]})
        res.update({"option2": o1_list[0]})
        res.update({"question3": q2_list[0]})
        res.update({"option3": o2_list[0]})
        res.update({"question4": q3_list[0]})
        res.update({"option4": o3_list[0]})

        return JsonResponse(res)


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


class RecommendView(APIView):

    def post(self, request, format=None):
        ans = request.data['ans']

        r = Alcohol.objects.filter(type_name__contains=ans)
        if r.count() > 1:
            res_json = json.dumps([x.to_dict() for x in r], ensure_ascii=False)
            res = json.loads(res_json, object_pairs_hook=OrderedDict)
            res_json = json.dumps(res[random.randrange(r.count())], ensure_ascii=False)
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

        res = OrderedDict()
        answer = ["answer1", "answer2", "answer3"]
        i = 0
        for c in cocktail:
            r = Alcohol.objects.filter(alcohol_id=c + 1)
            ans_json = json.dumps([x.to_dict() for x in r], ensure_ascii=False)
            res.update({answer[i]: json.loads(ans_json, object_pairs_hook=OrderedDict)[0]})
            i += 1

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
