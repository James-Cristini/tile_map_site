from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.title
