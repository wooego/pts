# coding:utf-8

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Question, Answer, MasterStatus
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def question(request):
    specialty = request.user.profile.specialty
    position = request.user.profile.position
    if request.session.get('dmq', None) is None: # dmq -> display mastered question
        if 'display_master' in request.POST:  # 不显示已经掌握的问题
            request.session['dmq'] = False
        else:
            request.session['dmq'] = True
    if request.session.get('each_page', None) is None:
        request.session['each_page'] = request.POST.get('each_page', 1)  # 每次都重新取值，该值会丢失！！！！！！！,使用全局变量解决
    """
    cur = connection.cursor()
    cur.execute("
    select * from practice_question q, practice_masterstatus m where q.id = m.question_id and is_master = 1
    ")
    questions_list = cur.fetchall()
    """
    if request.session.get('dmq'):
        query = 'select q.* from practice_question q, practice_masterstatus m where m.user_id = ' + str(
            request.user.id) + \
                ' and q.id = m.question_id and q.specialty ="' + str(specialty) + \
                '" and q.position ="' + str(position) + '" and is_master = 0 order by q.id'
    else:
        query = 'select q.* from practice_question q, practice_masterstatus m where m.user_id = ' + str(
            request.user.id) + ' and q.id = m.question_id order by q.id'

    #print '--------------\n' + query + '\n--------------------\n'
    questions_list = Question.objects.raw(query)
    # questions_list = Question.objects.all()#filter(specialty = Question.JUNXIE).filter( position = Question.FDZ)
    # select * from practice_question q, practice_masterstatus m where q.id = m.question_id and is_master = 0
    answers_list = []

    paginator = Paginator(list(questions_list), request.session.get('each_page'))  # 如果不加上list转化，会报RawQuerySet没有len()函数

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    for question in questions:
        answers = Answer.objects.filter(question_id=question.id)  # .order_by('option')
        answers_list.append(answers)
    # print(questions)
    # print(answers_list)
    return render(request, 'practice/practice.html', {"questions": questions, "answers_list": answers_list})


# Create your views here.
def master(request):
    qid = request.GET.get('qid')
    userid = request.GET.get('userid')
    ismaster = int(request.GET.get('ismaster'))

    user = User.objects.get(pk=userid)
    question = Question.objects.get(pk=qid)
    try:
        m = MasterStatus.objects.get(user=user, question=question)
    except ObjectDoesNotExist:
        m = MasterStatus.objects.create(user=user, question=question, is_master=ismaster)
        m.save()
    else:
        MasterStatus.objects.filter(user=user, question=question).update(is_master=ismaster)
    # m.save()
    return HttpResponse("Test")
