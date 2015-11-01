from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    Regulations = 'RL'
    HighTech = 'HT'
    Domain = 'DM'
    DomainPrimary = 'DP'
    TYPE_CHOICES = (
        (Regulations, '法规'),
        (HighTech, '高科技'),
        (Domain, '专业'),
        (DomainPrimary, '专业基础')
    )

    JUNXIE = 'JX'
    HANGDIAN = 'HD'
    JIXIE = 'XE'
    SPECIALTY_CHOICES = (
        (JUNXIE, '军械'),
        (HANGDIAN, '航电'),
        (JIXIE, '机械'),
    )

    FDZ = 'FDZ'
    SHI = 'SHI'
    YUAN = 'YUAN'
    POSITION_CHOICES = (
        (FDZ, '分队长以上'),
        (SHI, '师'),
        (YUAN, '员'),
    )

    content = models.CharField(max_length=300)  # 题目内容
    rightOption = models.CharField(max_length=4)  # 最多有四个正确选项
    specialty = models.CharField(max_length=2,
                                 choices=SPECIALTY_CHOICES, )
    position = models.CharField(max_length=4,
                                choices=POSITION_CHOICES, )
    type = models.CharField(max_length=2,
                            choices=TYPE_CHOICES, )
    # default=Regulations)

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question)
    option = models.CharField(max_length=1)  # 答案选项，如ABCD
    content = models.CharField(max_length=200)  # 答案的内容

    def __str__(self):
        return self.option+":"+self.content

    class Meta:
        ordering = ['question','option']

class MasterStatus(models.Model):
    user = models.OneToOneField(User)
    question = models.OneToOneField(Question)
    is_master = models.BooleanField(default=False)

# Create your models here.