from django.contrib import admin

from .models import Account, Alcohol, Question, Option, Answer


@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    pass


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