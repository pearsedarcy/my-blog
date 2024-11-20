from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', null=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.user.username