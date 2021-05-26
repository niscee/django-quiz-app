from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to="Slider")
    
    def __str__(self):
        return str(self.image)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url