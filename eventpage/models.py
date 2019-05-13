from django.db import models
from django.utils import timezone


class Info(models.Model):
    webtoon = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    # def __str__(self):
    #     return self.name