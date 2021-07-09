from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields ='__all__'
        exclude=('course_enrolled','now_attending',)

class CourseBatchForm(ModelForm):
    class Meta:
        model = StudentCourseData
        fields = '__all__'
        
class TaskForm(ModelForm):
    class Meta:
        model = TrainerTask
        fields = ['title','description','complete']


class TrainerRegistersForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']
