from django.db import models
from django.conf import settings

# Create your models here.
class CourseCategory(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    detail = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return str(self.name)



class CourseDetail(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseCategory,
        on_delete=models.CASCADE, verbose_name = 'Course Category')
    name = models.CharField(max_length=200, blank=False, null=False, default="--") 
    detail = models.CharField(max_length=200, blank=True, null=True)    
    pdf  = models.FileField(upload_to='course-files', blank=True, null=True)
    image = models.ImageField(upload_to="course-images", blank=True, null=True)
    video = models.URLField(max_length=200, blank=True, null=True) 
     


    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url    


            




# product model.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default="")
    detail = models.TextField(blank=True, null=True, default="")
    CourseCategory_id = models.ForeignKey(CourseCategory,
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Products")
    price = models.CharField(max_length=200, blank=True, null=True, default="")
    qty = models.BigIntegerField(blank=True, null=True, default=1)


    def __str__(self):
        return str(self.name)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



    
