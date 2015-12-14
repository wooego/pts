#coding:utf-8
from django.http import HttpResponse
from exam.models import PaperPartsPercent, ResultRecord
from django.contrib.auth.models import User
from practice.models import Question, Answer
from django.shortcuts import render
from django.db.models import Q
from time import time
from datetime import datetime


def exam(request):
    specialty = request.user.profile.specialty
    position = request.user.profile.position
    percents = PaperPartsPercent.objects.all()[0] #
    #domains = Question.objects.filter(specialty=specialty, position=position, type=Question.Domain).order_by('?').all().count()#[percents.domain]
    domains = Question.objects.filter(Q(specialty=specialty)|Q(specialty='AL'),\
                                      Q(position=position)|Q(position='AL'),\
                                      Q(type=Question.Domain))\
                                    .order_by('?').all()[0:percents.domain]
    #regulations = Question.objects.filter(specialty=specialty, position=position, type=Question.Regulations).order_by('?').all().count()#[percents.regulation]
    #domainprimarys= Question.objects.filter(specialty=specialty, position=position, type=Question.DomainPrimary).order_by('?').all().count()#[percents.domainprimary]
    regulations = Question.objects.filter(Q(specialty=specialty)|Q(specialty='AL'),\
                                      Q(position=position)|Q(position='AL'),\
                                      Q(type=Question.Regulations))\
                                    .order_by('?').all()[0:percents.regulation]
    domainprimarys = Question.objects.filter(Q(specialty=specialty)|Q(specialty='AL'),\
                                      Q(position=position)|Q(position='AL'),\
                                      Q(type=Question.DomainPrimary))\
                                    .order_by('?').all()[0:percents.domainprimary]
    #print type(domains), type(regulations), type(domainprimarys)

    domains = list(domains)
    regulations= list(regulations)
    domainprimarys = list(domainprimarys)
    domainprimarys.extend(regulations)
    domainprimarys.extend(domains)
    questions = domainprimarys

    answers_list = []
    for question in questions:
        answers = Answer.objects.filter(question_id=question.id)  # .order_by('option')
        answers_list.append(answers)
    #print question
    #print '###############'
    #print answers_list
    return render(request, 'exam/exam.html', {"questions": questions,"answers_list": answers_list,"start_time":int(time())})


def record(request):
    userid = request.GET.get('userid')
    score = int(request.GET.get('score'))
    seconds_used = int(request.GET.get('seconds_used'))
    user = User.objects.get(pk=userid)

    rr = ResultRecord.objects.create(user=user, score=score, seconds_used=seconds_used,time_examed=datetime.now())
    rr.save()
    return HttpResponse("stored")


def result(request):
    #return HttpResponse(request.POST.items())
    wrongs = 0
    question_list=[]
    post_data = request.POST
    for item in post_data.items():
        #print item[0],type(item[0]),'--->',item[1],type(item[1])
        if item[0].startswith('ro'):
            opt = item[0][2:]
            if post_data.get(opt) != post_data.get(item[0]):
                question_list.append(opt)
                wrongs += 1
    ret = '共错了 '+str(wrongs)+' 道题\n+'+str(sorted([int(x) for x in question_list]))
    return HttpResponse(ret)
