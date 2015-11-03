from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Question, Answer, MasterStatus
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

each_page = 1 #

def question(request):
    specialty = request.user.profile.specialty
    position = request.user.profile.position
    global each_page
    http_each_page = request.POST.get('each_page',1)#每次都重新取值，该值会丢失！！！！！！！,使用全局变量解决
    if http_each_page != 1 and  http_each_page != each_page:
        each_page = http_each_page
    questions_list = Question.objects.all()#filter(specialty = Question.JUNXIE).filter( position = Question.FDZ)
    answers_list = []

    paginator = Paginator(questions_list, each_page)

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
    #print(answers_list)
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
        m = MasterStatus.objects.create(user=user, question=question,is_master=ismaster)
        m.save()
    else:
       MasterStatus.objects.filter(user=user,question=question).update(is_master=ismaster)
    #m.save()
    return HttpResponse("Test")
