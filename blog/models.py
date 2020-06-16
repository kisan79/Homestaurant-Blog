from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver
from myadmin.models import Admin


# Models For blog App
# Post Model

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    pic1 = models.ImageField(upload_to='blogs_photos/', blank=True, null=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

#For Deleting The Images after the post is deleted
@receiver(post_delete,sender=Post)
def submission_delete(sender,instance,**kwargs):
    instance.pic1.delete(False)