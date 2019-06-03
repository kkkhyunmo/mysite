from django.db import models
from django.utils import timezone


class dbinfo(models.Model):
    name = models.CharField(unique=True, max_length=100)
    phone = models.CharField(unique=True, max_length=11)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name