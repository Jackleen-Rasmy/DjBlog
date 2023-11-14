from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


'''
-title
-content
-draft
-publish date
-author
-image
-tags
-category
-comments
'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='author_post', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post',blank=True,null=True)
    tags = TaggableManager()
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.post)

    
    
    
    
    
    
