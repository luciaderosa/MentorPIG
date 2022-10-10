from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    img_path = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
