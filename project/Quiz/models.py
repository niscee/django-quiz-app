from django.db import models
from CourseCategory.models import CourseCategory

# Create your models here.
class Question(models.Model):
    course_id = models.ForeignKey(CourseCategory,
        on_delete=models.CASCADE, verbose_name = 'Course Category')
    question = models.TextField(default="", blank=False, null=False)
    option1 = models.CharField(max_length=200, blank=False, null=False, default="")
    option2 = models.CharField(max_length=200, blank=False, null=False, default="")
    option3 = models.CharField(max_length=200, blank=False, null=False, default="")
    option4 = models.CharField(max_length=200, blank=False, null=False, default="")
    answer = models.CharField(max_length=200, blank=False, null=False, default="")  


    def __str__(self):
        return self.course_id



 


