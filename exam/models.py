# coding:utf-8
from django.core.exceptions import ValidationError

from django.db import models


class PaperPartsPercent(models.Model):
    domain = models.IntegerField(verbose_name='专业基础题比例', )
    regulation = models.IntegerField(verbose_name='法规题比例', )
    domainprimary = models.IntegerField(verbose_name='专业题比例', )


    def __str__(self):
        return str(self.regulation) + ":" + str(self.domain) + ":" + str(self.domainprimary)

    def __unicode__(self):
        return str(self.regulation) + ":" + str(self.domain) + ":" + str(self.domainprimary)

    def clean(self):
        if self.regulation + self.domain + self.domainprimary != 100:
            raise ValidationError('题目比例不正确，请保证其和为100')


# Create your models here.
