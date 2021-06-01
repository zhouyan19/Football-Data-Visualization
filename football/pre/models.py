from django.db import models

# Create your models here.
class Match(models.Model):
    date=models.DateTimeField()
    home_name=models.CharField(max_length=100)
    away_name=models.CharField(max_length=100)
    home_score=models.IntegerField()
    away_name=models.IntegerField()
    tournament=models.CharField(max_length=100)