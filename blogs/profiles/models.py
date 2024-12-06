from django.db import models
from posts.models import User
from posts.models import user_directory_path
from django.db.models.signals import post_save

# Create your models here.



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        if (self.user.first_name) and (self.user.last_name):
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return f"{self.user.username}"

        

        


# If user is created, automatically make them a profile

def user_created_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    pass

post_save.connect(user_created_signal, sender=User)
