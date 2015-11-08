# coding:utf-8
from django import forms
# from django.contrib.auth.models import User

class ConfigureForm(forms.Form):
    each_page = forms.IntegerField(
        required=True,
        min_value=1,
        label=u"每页显示的题目数量",
        error_messages={'required': u'请输入每页显示的题目数量'},
        widget=forms.NumberInput(
            attrs={
                'placeholder': u"每页显示的题目数量,如 1",
            }
        ),
    )
    dmp = forms.BooleanField(
        label=u"显示已经掌握的题目",
        initial=True,
        widget=forms.CheckboxInput(),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"请按要求输入数据")
        else:
            cleaned_data = super(ConfigureForm,self).clean()