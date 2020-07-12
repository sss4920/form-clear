from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '쓴사람:'+str(self.author)