from django.db import models

# Create your models here.


class Hotdog(models.Model):
    name = models.CharField(max_length=60)
    link = models.URLField()

    def __str__(self):
        return self.name
