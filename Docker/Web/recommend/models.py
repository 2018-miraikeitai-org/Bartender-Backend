#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models
from collections import OrderedDict


class Account(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    mailaddress = models.TextField()
    login_pw = models.CharField(max_length=20)

    def to_dict(self):
        add = (('user_id', self.user_id),
               ('user_name', self.user_name),
               ('mailaddress', self.mailaddress),
               ('login_pw', self.login_pw))

        return OrderedDict(add)

    class Meta:
        managed = False
        db_table = 'account'


class Alcohol(models.Model):
    alcohol_id = models.IntegerField(primary_key=True)
    type_name = models.TextField()  # This field type is a guess.
    alco_name = models.CharField(max_length=20)
    image = models.TextField(blank=True, null=True)
    detail = models.TextField()

    def to_dict(self):
        add = (('alcohol_id', self.alcohol_id),
               ('alco_name', self.alco_name),
               ('image', self.image),
               ('detail', self.detail))

        return OrderedDict(add)

    class Meta:
        managed = False
        db_table = 'alcohol'


class Question(models.Model):
    ques_id = models.IntegerField(primary_key=True)
    ques_contents = models.CharField(max_length=30)

    def to_dict(self):
        add = (('ques_id', self.ques_id),
               ('ques_contents', self.ques_contents))

        return OrderedDict(add)

    class Meta:
        managed = False
        db_table = 'question'


class Option(models.Model):
    option_id = models.IntegerField(primary_key=True)
    ques = models.ForeignKey('Question', models.DO_NOTHING)
    option_contents1 = models.CharField(max_length=30)
    option_contents2 = models.CharField(max_length=30)
    option_contents3 = models.CharField(max_length=30, blank=True, null=True)
    option_contents4 = models.CharField(max_length=30, blank=True, null=True)

    def to_dict(self):
        add = (('option_id', self.option_id),
               ('option_contents1', self.option_contents1),
               ('option_contents2', self.option_contents2),
               ('option_contents3', self.option_contents3),
               ('option_contents4', self.option_contents4))

        return OrderedDict(add)

    class Meta:
        managed = False
        db_table = 'option'
        unique_together = (('option_id', 'ques'),)


class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Account', models.DO_NOTHING)
    option_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    learning_data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'answer'
        unique_together = (('answer_id', 'user'),)
