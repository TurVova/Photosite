from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return (self.name + " " + self.last_name)

    class Meta:
        ordering = ["-create", ]
        
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    slug = models.SlugField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-create", ]