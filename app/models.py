from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime


# Create your models here.

class QuestionManager(models.Manager):
    def get_questions_by_tag(self, tag_name):
        tag_item = Tag.objects.filter(name=tag_name)
        return Question.objects.filter(tags__in=tag_item)

    def newest(self):
        return self.order_by('-creation_time')

    def get_answers_count(self):
        answers = Answer.objects.filter(question=self)
        return answers.count()

    def sort_by_rating(self):
        return self.all()

    #def get_questions_by_tag(self, tag_item):


class Question(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', related_name='questions')
    creation_time = models.DateTimeField(default=datetime.now, blank=True)

    objects = QuestionManager()

    def __str__(self):
        return f"{self.title}"


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    avatar = models.ImageField()

    def __str__(self):
        return f"{self.user.username}"


class TagManager(models.Manager):
    pass

class Tag(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)

    objects = TagManager()

    def __str__(self):
        return f"{self.name}"


class AnswerManager(models.Manager):
    def get_answers_for_question(self, question):
        return self.filter(question=question)

class Answer(models.Model):
    content = models.TextField()
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    question = models.ForeignKey('Question', max_length=256, on_delete=models.PROTECT)

    objects = AnswerManager()