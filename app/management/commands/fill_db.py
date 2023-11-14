from django.core.management.base import BaseCommand
from app.models import Question, Profile, Answer, Tag, QuestionRate, AnswerRate
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Fill database for Question-Answer app'

    def add_arguments(self, parser):
        parser.add_argument('--ratio', type=int)

    def handle(self, *args, **options):

        ratio = options['ratio']

        password = 'pass_new_test_123_1'
        users = [None] * ratio
        profiles = [None] * ratio
        for i in range(ratio):
            users[i] = User(username='user' + str(i + 1),
                            password=password)
            users[i].save()
            profiles[i] = Profile(user=users[i])
            profiles[i].save()

        tags = [None] * ratio
        for i in range(ratio):
            tags[i] = Tag(name='tag' + str(i + 1))
            tags[i].save()

        questions = [None] * (ratio * 10)
        for i in range(ratio * 10):
            questions[i] = Question(title='Question №' + str(i+1),
                                    content='Question text ' * 20,
                                    author=profiles[i % ratio])
            questions[i].save()
            questions[i].tags.add(tags[i % (ratio - 1)], tags[i % (ratio - 1) + 1])
            questions[i].save()

        answers = [None] * (ratio * 100)
        for i in range(ratio * 100):
            answers[i] = Answer(content='Answer text ' * 20,
                                author=profiles[i % ratio],
                                question=questions[i % (ratio * 10)])
            answers[i].save()


        for i in range(ratio * 200):
            q_rate = QuestionRate(is_positive=True,
                                  question=questions[i % (ratio * 10)],
                                  user=profiles[i % ratio])
            q_rate.save()
            a_rate = AnswerRate(is_positive=True,
                                answer=answers[i % (ratio * 100)],
                                user=profiles[i % ratio])
            a_rate.save()
