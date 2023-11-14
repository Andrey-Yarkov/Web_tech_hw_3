import django.contrib.admin
from django.contrib import admin
from .models import Question, Profile, Answer, Tag, QuestionRate, AnswerRate

# Register your models here.

admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(QuestionRate)
admin.site.register(AnswerRate)