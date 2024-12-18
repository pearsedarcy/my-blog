from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    exerpt = models.TextField(max_length=100, default="", blank=True)
    cover_image = CloudinaryField('image', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.title} | {self.author.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ["approved", "created"]

    def __str__(self):
        return f"{self.approved} Comment by {self.author.username} on {self.post.title}"

    def approved_status(self):
        return self.approved
    approved_status.boolean = True
    approved_status.short_description = 'Approved'

