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
    hightechs= Question.objects.filter(specialty=specialty, position=position, type=Question.HighTech).order_by('?').all()#[percents.hightech]
    domainprimarys= Question.objects.filter(specialty=specialty, position=position, type=Question.DomainPrimary).order_by('?').all()#[percents.domainprimary]

    questions = domains | regulations | hightechs | domainprimarys
    answers_list = []
    for question in questions:
        answers = Answer.objects.filter(question_id=question.id)  # .order_by('option')
        answers_list.append(answers)
    return render(request, 'exam/exam.html', {"questions": questions,"answers_list": answers_list})
