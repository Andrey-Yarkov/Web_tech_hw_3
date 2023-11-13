from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import Question, Tag, Answer

# global data
def paginate(object, page, per_page=5):
    paginator = Paginator(object, per_page)
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        # If the page is empty, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    return page_obj


# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    questions = Question.object.all()
    return render(request, 'index.html', context={'questions': paginate(questions, page)})


def tag(request, tag_name):
    page = request.GET.get('page', 1)
    tag_item = Tag.object.filter(name=tag_name)
    questions = Question.object.filter(tags__in=tag_item)
    return render(request, 'tag.html', context={'tag': tag_name, 'questions_by_tag': paginate(questions, page)})


def hot(request):
    page = request.GET.get('page', 1)
    hot_questions = Question.object.sort_by_rating()
    return render(request, 'hot.html', context={'hot_questions': paginate(hot_questions, page)})


def question(request, question_id):
    page = request.GET.get('page', 1)
    question_item = Question.object.get(pk=question_id)
    answers = Answer.object.filter(question=question_item)
    return render(request, 'question.html',
                  context={'question': question_item,
                           'answers': paginate(answers, page)})


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
