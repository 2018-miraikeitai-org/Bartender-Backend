from django.db import models


class Account(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=-1)
    mailaddress = models.CharField(max_length=-1)
    login_pw = models.CharField(max_length=-1)


class Alcohol(models.Model):
    alcohol_id = models.IntegerField(primary_key=True)
    type_name = models.TextField()  # This field type is a guess.
    alco_name = models.CharField(max_length=-1)
    image = models.CharField(max_length=-1, blank=True, null=True)
    detail = models.CharField(max_length=-1, blank=True, null=True)


class Question(models.Model):
    ques_id = models.IntegerField(primary_key=True)
    ques_contents = models.CharField(max_length=-1)


class Option(models.Model):
    option_id = models.IntegerField(primary_key=True)
    ques = models.ForeignKey('Question', models.DO_NOTHING)
    option_contents1 = models.CharField(max_length=-1)
    option_contents2 = models.CharField(max_length=-1)
    option_contents3 = models.CharField(max_length=-1)
    option_contents4 = models.CharField(max_length=-1, blank=True, null=True)
