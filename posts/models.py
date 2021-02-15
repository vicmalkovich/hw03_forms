from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title



class Post(models.Model):
    text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)


