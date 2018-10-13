from django.db import models


class Account(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    mailaddress = models.TextField()
    login_pw = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account'


class Alcohol(models.Model):
    alcohol_id = models.IntegerField(primary_key=True)
    type_name = models.TextField()  # This field type is a guess.
    alco_name = models.CharField(max_length=20)
    image = models.TextField(blank=True, null=True)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'alcohol'


class Question(models.Model):
    ques_id = models.IntegerField(primary_key=True)
    ques_contents = models.CharField(max_length=30)

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
