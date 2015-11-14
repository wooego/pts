# coding:utf-8
from django.http import HttpResponse
from exam.models import PaperPartsPercent
from practice.models import Question, Answer
from django.shortcuts import render


def exam(request):
    specialty = request.user.profile.specialty
    position = request.user.profile.position
    percents = PaperPartsPercent.objects.all()[0] #
    domains = Question.objects.filter(specialty=specialty, position=position, type=Question.Domain).order_by('?').all()#[percents.domain]
    regulations = Question.objects.filter(specialty=specialty, position=position, type=Question.Regulations).order_by('?').all()#[percents.regulation]
    domainprimarys= Question.objects.filter(specialty=specialty, position=position, type=Question.DomainPrimary).order_by('?').all()#[percents.domainprimary]

    questions = domains | regulations | domainprimarys
    answers_list = []
    for question in questions:
        answers = Answer.objects.filter(question_id=question.id)  # .order_by('option')
        answers_list.append(answers)
    return render(request, 'exam/exam.html', {"questions": questions,"answers_list": answers_list})


def result(request):
    #return HttpResponse(request.POST.items())
    wrongs = 0
    post_data = request.POST
    for item in post_data.items():
        #print item[0],type(item[0]),'--->',item[1],type(item[1])
        if item[0].startswith('ro'):
            opt = item[0][2:]
            if post_data.get(opt) != post_data.get(item[0]):
                wrongs += 1
    ret = '共错了 '+str(wrongs)+' 道题\n'
    return HttpResponse(ret)
