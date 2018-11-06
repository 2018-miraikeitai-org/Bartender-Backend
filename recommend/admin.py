#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib import admin

from .models import Alcohol, Question, Option, Answer


@admin.register(Alcohol)
class Entry(admin.ModelAdmin):
    pass


@admin.register(Question)
class Entry(admin.ModelAdmin):
    pass


@admin.register(Option)
class Entry(admin.ModelAdmin):
    pass


@admin.register(Answer)
class Entry(admin.ModelAdmin):
    pass