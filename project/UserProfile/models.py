from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    STUDENT = 'STD'
    TEACHER = 'TEC'
    ADMIN = 'ADM'

    USER_TYPES = [
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (ADMIN, 'admin'),
    ]

    address = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="UserProfile", null=True, blank=True)
    user_id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    user_type=models.CharField(
        max_length=3,
        choices=USER_TYPES,
        default=STUDENT,
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url     
    


# django signal userprofile creation on user registration.
User = settings.AUTH_USER_MODEL
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:     
        UserProfile.objects.create(user_id=instance)
    
    
