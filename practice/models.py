# coding:utf-8

from django.db import models
from django.contrib.auth.models import User


'''
class RandomManager(models.Manager):
    def get_queryset(self):
        return super(RandomManager, self).get_queryset().order_by('?')
'''


class Question(models.Model):
    Regulations = 'RL'
    Domain = 'DM'
    DomainPrimary = 'DP'
    TYPE_CHOICES = (
        (Regulations, '法规'),
        (Domain, '专业'),
        (DomainPrimary, '专业基础')
    )

    JIXIE = 'XE'
    JUNXIE = 'JX'
    TESHE = 'TS'
    WUXIANDIAN = 'WX'
    ALL = 'AL'
    SPECIALTY_CHOICES = (
        (ALL, '所有专业'),
        (JIXIE, '机械'),
        (JUNXIE, '军械'),
        (TESHE,'特设'),
        (WUXIANDIAN,'无线电'),
    )

    FDZ = 'FDZ'
    SHI = 'SHI'
    YUAN = 'YUAN'
    ALL = 'ALL'
    POSITION_CHOICES = (
        (ALL, '所有人员'),
        (FDZ, '分队长以上'),
        (SHI, '师'),
        (YUAN, '员'),
    )

    content = models.CharField(max_length=300, verbose_name=u'题目内容')  # 题目内容
    rightOption = models.CharField(max_length=4)  # 最多有四个正确选项
    specialty = models.CharField(max_length=2,
                                 choices=SPECIALTY_CHOICES, )
    position = models.CharField(max_length=4,
                                choices=POSITION_CHOICES, )
    type = models.CharField(max_length=2,
                            choices=TYPE_CHOICES, )
    # default=Regulations)

    #randoms = RandomManager()

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question)
    option = models.CharField(max_length=1)  # 答案选项，如ABCD
    content = models.CharField(max_length=200)  # 答案的内容

    def __str__(self):
        return self.option + ":" + self.content

    def __unicode__(self):
        return self.option + ":" + self.content

    class Meta:
        ordering = ['question', 'option']


class MasterStatus(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    is_master = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ":" + self.question.content + ":" + str(self.is_master)

    def __unicode__(self):
        return self.user.username + ":" + self.question.content + ":" + str(self.is_master)

# Create your models here.
