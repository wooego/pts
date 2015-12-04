#coding:utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pts.settings')

import django

django.setup()

from practice.models import Question, Answer
from accounts.models import UserProfile
from random import randint


specialties = (
"AL","XE","TS","WX","JX"
)
positions = (
"AL","FDZ","SHI","YUAN"
)
qtype = (
"RL","DP","DM"
)

def genRandomRightOption():
    len = randint(0,3)
    opt = chr(ord('A')+len)
    return opt,len

def genRandomSpecialty():
    return specialties[randint(0,4)]

def genRandomPosition():
    return positions[randint(0,3)]

def genRandomQtype():
    return qtype[randint(0,2)]
    
def populate(nums=10):
    add_userprofile(1,'JX','FDZ')
    questions = []
    for i in range(nums):
        questions.append("问题"+str(i+1)+"?")
    for i,con in enumerate(questions):
        opt,index= genRandomRightOption()
        q=add_question(con,opt,genRandomSpecialty(),genRandomPosition(),genRandomQtype())
        for j in range(4):
            if j != index:
                add_answer(q.id,chr(ord('A')+j),"答案"+str(j+1))
            else:
                add_answer(q.id,chr(ord('A')+j),"正确答案"+str(j+1))

def add_question(con, ro, spec, pos,qtype):
    q = Question.objects.get_or_create(content=con, rightOption=ro,specialty=spec,position=pos,type=qtype)[0]
    return q


def add_answer(qid,opt,con):
    a = Answer.objects.get_or_create(question_id=qid, option=opt, content=con)[0]
    return a

def add_userprofile(uid,spec,pos):
    u = UserProfile.objects.get_or_create(specialty=spec,position=pos,user_id=uid)[0]
    return u

if __name__ == '__main__':
    print("Starting pts population script ...")
    populate(1000)
