from __future__ import unicode_literals

from django.db import models

class Tile(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    story = models.TextField(blank=True)
    horiz_position = models.IntegerField()
    vert_position = models.IntegerField()
    location = models.CharField(max_length=50)
    tradegoods = models.ManyToManyField('Tradegood', blank=True)
    organizations = models.ManyToManyField('Organization', blank=True)
    relevant_places = models.ManyToManyField('Place', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_number = models.IntegerField()

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('question_number',)


class Person(models.Model):
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    occupation = models.CharField(max_length=75)
    description = models.TextField()
    quote = models.TextField()
    locations = models.ManyToManyField('Place')
    tile = models.CharField(max_length=15)
    image_name = models.CharField(max_length=75)
    #places = models.ManyToManyField("Place")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Place(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    parent_location = models.ForeignKey('Place', blank=True)
    place_type = models.CharField(max_length=50)
    image_name = models.CharField(max_length=75)
    tiles = models.ManyToManyField("Tile", blank=True)
    is_world = models.BooleanField(verbose_name="Is this place your 'World' in which all other locations exist?")

    def save(self, *args, **kwargs):
        if self.is_world:
            try:
                temp = Place.objects.get(is_world=True)
                if self != temp:
                    temp.is_world=False
                    temp.parent_location=self
                    self.parent_location=self
                    temp.save()
            except Place.DoesNotExist:
                pass

        super(Place, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Tradegood(models.Model):
    name = models.CharField(max_length=50)
    goods_type = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    image_name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Organization(models.Model):
    name = models.CharField(max_length=50)
    organization_type = models.CharField(max_length=50)
    description = models.TextField()
    associated_tiles = models.ManyToManyField('Tile', blank=True)
    locations = models.ManyToManyField('Place', blank=True)
    image_name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Culture(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    image_name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class WorkOfArt(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    excerpt = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=50)
    image_name = models.CharField(max_length=75)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
