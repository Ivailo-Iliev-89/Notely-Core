from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25,default='info')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=20, default='secondary')

    def __str__(self):
        return self.name


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='notes_with_tag')
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True,related_name='category_notes')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} ({self.owner.username})'

