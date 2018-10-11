# coding: utf-8
from rest_framework import serializers

from .models import Account, Alcohol, Question, Option, Answer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_name', 'mailaddress', 'login_pw')


class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = ('alcohol_id', 'type_name', 'alco_name', 'image', 'detail')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = 'ques_contents'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('option_contents1', 'option_contents2', 'option_contents3', 'option_contents4')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
