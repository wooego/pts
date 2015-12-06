from django.contrib import admin
from .models import UserProfile
from practice.models import Question, Answer, MasterStatus
from exam.models import PaperPartsPercent, ResultRecord

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'specialty','position')

admin.site.register(UserProfile, UserProfileAdmin)

# Register your models here.

class QustionAdmin(admin.ModelAdmin):
    exclude = []
admin.site.register(Question, QustionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    exclude = []
admin.site.register(Answer, AnswerAdmin)

class MasterStatusAdmin(admin.ModelAdmin):
    exclude = []
admin.site.register(MasterStatus, MasterStatusAdmin)

class PaperPartsPercentAdmin(admin.ModelAdmin):
    exclude = []
admin.site.register(PaperPartsPercent, PaperPartsPercentAdmin)

class ResultRecordAdmin(admin.ModelAdmin):
    exclude = []
admin.site.register(ResultRecord, ResultRecordAdmin)
