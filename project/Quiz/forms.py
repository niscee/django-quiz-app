from .models import Question, QuizPoint
from django import forms



class QuizForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class QuizPointForm(forms.ModelForm):
    class Meta:
        model = QuizPoint
        fields = ['feedback']     