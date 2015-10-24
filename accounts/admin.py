from django.contrib import admin
from .models import UserProfile, Question, Answer, MasterStatus

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
