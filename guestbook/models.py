from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name        = models.CharField(max_length=50)
    comment     = models.TextField(max_length=1)
    date_added  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name