from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime


# Create your models here.

class QuestionManager(models.Manager):
    def sort_by_time(self):
        return self.order_by('-creation_time')

    def get_answers_count(self):
        answers = Answer.object.filter(question=self)
        return answers.count()

    def sort_by_rating(self):
        return self.all()

    #def get_questions_by_tag(self, tag_item):


class Question(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', related_name='questions')
    #creation_time = models.DateTimeField()

    object = QuestionManager()

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

    object = TagManager()

    def __str__(self):
        return f"{self.name}"


class AnswerManager(models.Manager):
    pass

class Answer(models.Model):
    content = models.TextField()
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    question = models.ForeignKey('Question', max_length=256, on_delete=models.PROTECT)

    object = AnswerManager()