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
            users[i] = User(username='user' + str(i + 1), password=password)
            users[i].save()
            profiles[i] = Profile(user=users[i])
            profiles[i].save()

        tags = [None] * ratio
        for i in range(ratio):
            tags[i] = Tag(name='tag' + str(i + 1))
            tags[i].save()

        question_titles = ['A', 'B', 'C', 'D', 'E', 'F', 'J']
        questions = [None] * (ratio * 10)
        for i in range(ratio * 10):
            questions[i] = Question(title=question_titles[i % 7] * (i % ratio + 1), content='QQ',
                                    author=profiles[i % ratio])
            questions[i].save()
            questions[i].tags.add(tags[i % (ratio - 1)], tags[i % (ratio - 1) + 1])
            questions[i].save()

        answers_content = ['H', 'I', 'J', 'K', 'L', 'M', 'N']
        answers = [None] * (ratio * 100)
        for i in range(ratio * 100):
            answers[i] = Answer(content=answers_content[i % 7] * (i % ratio + 1), author=profiles[i % ratio],
                                question=questions[i % (ratio * 10)])
            answers[i].save()


        #ans_rate = AnswerRate(is_positive=True, answer=answer, user=user1)
        #ans_rate.save()
        #qu_rate = QuestionRate(is_positive=False, question=question, user=user2)
        #qu_rate.save()
