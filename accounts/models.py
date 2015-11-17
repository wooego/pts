# coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
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
    user = models.OneToOneField(User, related_name='profile')
    specialty = models.CharField(max_length=2,
                                 choices=SPECIALTY_CHOICES, )
    position = models.CharField(max_length=4,
                                choices=POSITION_CHOICES, )

    def __unicode__(self):
        return self.user.username + " : " + self.specialty + " : " + self.position

'''
#如果保留下面的代码，会在管理界面创建一个User后，自动建立一个UserProfile,从而无法实现添加UserProfile实例，会
#提示已存在。只能修改。
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)
'''


