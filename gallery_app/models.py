from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=30)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False,
                              width_field='width',
                              height_field='height')
    create = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create", ]


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False,
                              width_field='width',
                              height_field='height')
    create = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create", ]
