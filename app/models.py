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

    #def get_answers_count(self):
    #    answers = Answer.objects.filter(question=self)
    #    return answers.count()

    def sort_by_rating(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', related_name='questions', blank=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    answers_count = models.IntegerField(default=0, blank=True)

    objects = QuestionManager()

    def __str__(self):
        return f"{self.title}"


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    avatar = models.ImageField(blank=True)
    user_rating = models.IntegerField(default=0, blank=True)

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

    def sort_by_rating(self):
        return self.order_by('-rating')

class Answer(models.Model):
    content = models.TextField()
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    question = models.ForeignKey('Question', max_length=256, on_delete=models.PROTECT)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    is_created = models.BooleanField(default=False)

    objects = AnswerManager()

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)
        if not self.is_created:
            self.is_created = True
            self.question.answers_count = self.question.answers_count + 1
            self.question.save()


class QuestionRateManager(models.Manager):
    def get_question_rate(self, question):
        rates = self.filter(question=question)
        positive_rates = rates.filter(is_positive=True)
        return 2 * positive_rates.count() - rates.count()

class QuestionRate(models.Model):
    is_positive = models.BooleanField(null=True, blank=True)
    question = models.ForeignKey('Question', max_length=256, on_delete=models.PROTECT)
    user = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)

    objects = QuestionRateManager()

    def save(self, *args, **kwargs):
        super(QuestionRate, self).save(*args, **kwargs)
        if (self.is_positive):
            self.question.rating = self.question.rating + 1
        else:
            self.question.rating = self.question.rating - 1
        self.question.save()


class AnswerRateManager(models.Manager):
    def get_answer_rate(self, answer):
        rates = self.filter(answer=answer)
        positive_rates = rates.filter(is_positive=True)
        return 2 * positive_rates.count() - rates.count()

class AnswerRate(models.Model):
    is_positive = models.BooleanField(null=True, blank=True)
    answer = models.ForeignKey('Answer', max_length=256, on_delete=models.PROTECT)
    user = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)

    objects = AnswerRateManager()

    def save(self, *args, **kwargs):
        super(AnswerRate, self).save(*args, **kwargs)
        if (self.is_positive):
            self.answer.rating = self.answer.rating + 1
        else:
            self.answer.rating = self.answer.rating - 1
        self.answer.save()