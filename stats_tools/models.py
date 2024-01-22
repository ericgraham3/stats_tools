from django.db import models


class RandomSample(models.Model):
    """Returns a set of random numbers to user"""
    min_value = models.IntegerField(max_length=100)
    max_value = models.IntegerField(max_length=100)
    rows = models.IntegerField(max_length=2000)
    columns = models.IntegerField(max_length=10)
    date_requested = models.DateTimeField(auto_now_add=True)

