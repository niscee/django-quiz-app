from django.contrib import admin
from .models import QuizAttempt, QuizPoint

# Register your models here.
admin.site.register(QuizAttempt)
admin.site.register(QuizPoint)