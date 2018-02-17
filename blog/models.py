from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
    
    def snippet(self):
        if len(self.text) >= 40:
            return self.text[:40] + ' ...'
        else:
            return self.text

    class Meta:
        ordering = ["-create", ]