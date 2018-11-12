#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from rest_framework import serializers

from .models import Alcohol, Question, Option, Answer, History

'''
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_name', 'mailaddress', 'login_pw')
'''


class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = ('alcohol_id', 'type_name', 'alco_name', 'image', 'detail')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('ques_id', 'ques_contents')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('option_id', 'ques_id', 'option_contents1', 'option_contents2', 'option_contents3', 'option_contents4')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_id', 'user_id', 'option_data', 'learning_data')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('history_id', 'user_id', 'alco_name', 'data_joined', 'review')
