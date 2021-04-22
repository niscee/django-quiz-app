from .models import Question
from django import forms



class QuizForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'