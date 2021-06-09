from django.db import models
from CourseCategory.models import CourseCategory
from django.conf import settings

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



# check quiz status and number of attempt
class QuizAttempt(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user_id) 


# check quiz status
class QuizPoint(models.Model):
    quizattempt_id = models.ForeignKey(QuizAttempt,
        on_delete=models.CASCADE)
    score = models.BigIntegerField(default=0) 
    percentage = models.BigIntegerField(default=0)
    feedback = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return str(self.score) 

    
    # calculate quiz point.
    def countScore(anscol):
        count = 0

        for i in anscol.keys():
            if i != "csrfmiddlewaretoken" and i != "quizattempt_id":
                id = int(i)
                q = Question.objects.get(id=id)
                if q.answer == anscol[i]:
                    count += 1
                else:
                    count += 0    
        
        return count

    # calculate quiz score percentage.
    def getPercentage(score, quesTotal):
        return (score*100)//quesTotal    

