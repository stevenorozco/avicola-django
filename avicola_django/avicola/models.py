from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Gallina(models.Model):
    edad = models.IntegerField()
    raza = models.CharField(max_length=100)

class