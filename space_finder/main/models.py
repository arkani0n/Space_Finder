from django.db import models
from django.urls import reverse
class Planet(models.Model):
    name = models.CharField('name the planet', max_length=50)
    description = models.TextField('Description of the planet')
    short_description= models.CharField('Short description', max_length=200)
    url = models.URLField('URL of picture for the planet', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planet_detail',kwargs={'pk':self.id})


class Star(models.Model):
    name = models.CharField('Name the star', max_length=50)
    description = models.TextField('Description of the star')
    short_description= models.CharField('Short description', max_length=200)
    url = models.URLField('URL of picture for the planet', null=True)
    star_system = models.ManyToManyField('Planet')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('star_detail',kwargs={'pk':self.id})