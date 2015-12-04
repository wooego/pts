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
        if 'dmp' in request.POST:  # 不显示已经掌握的问题
            request.session['dmq'] = False
        else:
            request.session['dmq'] = True
    if request.session.get('each_page', None) is None:
        request.session['each_page'] = request.POST.get('each_page', 1) 
    if request.session.get('question_type',None) is None:
        request.session['question_type'] = request.POST.get('question_type','AL') 
    if request.session['question_type'] == 'AL':
        request.session['question_type']='%' #用以匹配所有值
    """
    cur = connection.cursor()
    cur.execute("
    select * from practice_question q, practice_masterstatus m where q.id = m.question_id and is_master = 1
    ")
    questions_list = cur.fetchall()
    """
    if request.session.get('dmq'): #不显示已经掌握的问题
        #下面的query只能处理已经存在于practice_masterstatus表中，且is_master字段值为0的情况，不能处理不存在于该表中的数据
        query = 'select q.* from practice_question q, practice_masterstatus m where m.user_id = ' + str( request.user.id) + \
                ' and q.id = m.question_id and (q.specialty ="' + str(specialty) + \
                '" or q.specialty="AL") and (q.position ="' + str(position) + '" or q.position = "AL") and\
                q.type like "'+request.session['question_type']+'" and is_master != 1\
                order by q.id'
        #处理数据不在parctice_masterstatus表中的问题
        query2 = 'select * from practice_question  where id not in (select question_id from practice_masterstatus )'+\
                ' and  (specialty="'+ str(specialty) + '" or specialty="AL") and (position ="'+str(position) +'" or position="AL")\
                and practice_question.type like "'+request.session['question_type']+'"'
    else: #显示所有问题
        query = 'select * from practice_question where (specialty = "' + str(specialty) + \
        '" or specialty="AL") and (position ="' + str(position) + '" or position="AL") \
        and practice_question.type like "'+request.session['question_type']+'" order by id '
        query2 = None

    #print '--------------\n' + query + '\n--------------------\n'
    questions_list = Question.objects.raw(query)#此处question_list有可能为空,未处理
    if query2 is not None:
        questions_list2 = Question.objects.raw(query2)
        questions_list = list(questions_list)+ list(questions_list2)
    answers_list = []

    paginator = Paginator(list(questions_list), request.session.get('each_page'))  # 如果不加上list转化，会报RawQuerySet没有len()函数

    page = request.GET.get('page')
    status_dict = {}
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    for question in questions:
        answers = Answer.objects.filter(question_id=question.id)  # .order_by('option')
        answers_list.append(answers)
        masterstatus = MasterStatus.objects.filter(question_id = question.id).filter(user_id = request.user.id)
        if masterstatus.count() != 0:
            status_dict[question.id]=masterstatus[0].is_master
        else:
            status_dict[question.id]=False
    return render(request, 'practice/practice.html', {"questions": questions,"status_dict":status_dict,"answers_list": answers_list})


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
