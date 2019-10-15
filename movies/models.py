from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=100)
    score = models.FloatField()
    audience = models.IntegerField()
    open_date = models.DateField()
    poster_url = models.TextField()
    description = models.TextField()