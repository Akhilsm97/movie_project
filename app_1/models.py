from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.movie_name
