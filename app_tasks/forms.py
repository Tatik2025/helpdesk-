from django import forms
from app_tasks.models import Priority, Task, Department, Status,Type_task
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from datetime import datetime


class TaskDetailForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskDetailForm, self).__init__(*args, **kwargs)
        if user.access_level ==1:
            pass



    class_user = get_user_model()

    type_task_id = forms.ModelChoiceField(queryset=Type_task.objects, label="Тип Заявки", empty_label= "Не выбран тип заявки", widget=forms.Select(attrs={'class': 'form-control'}))
    theme  = forms.CharField(max_length=100, label="Тема", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тему заявки'}))
    priority_id = forms.ModelChoiceField(queryset=Priority.objects, label="Важность",initial = 1, widget=forms.Select(attrs={'class': 'form-control'}))
    status_id =  forms.ModelChoiceField(queryset=Status.objects, label="Статус", initial = 3, widget=forms.Select(attrs={'class': 'form-control'}))
    #department_id = forms.ModelChoiceField(queryset=Department.objects, label="Подразделение",widget=forms.Select(attrs={'class': 'form-control'}))
    user_id =  forms.ModelChoiceField(queryset=class_user.objects, label="Исполнитель", widget=forms.Select(attrs={'class': 'form-control'}))
    #author_id = forms.
    description = forms.CharField(max_length=1000, label="Описание", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание заявки'}))



    class Meta:
        fields=('type_task_id','theme','priority_id','status_id','description','user_id',)
