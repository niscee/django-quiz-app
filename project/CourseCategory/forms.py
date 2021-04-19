from .models import CourseDetail
from django import forms
from Authentication.models import CustomUser


class CourseDetailForm(forms.ModelForm):
    class Meta:
        model = CourseDetail
        exclude = ['user_id']


