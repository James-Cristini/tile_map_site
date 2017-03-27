from __future__ import unicode_literals

from django.db import models

class Tile(models.Model):
    title = models.CharField(max_length= 15)
    description = models.TextField()
    horiz_position = models.IntegerField()
    vert_position = models.IntegerField()

    def __str__(self):
        return self.title
