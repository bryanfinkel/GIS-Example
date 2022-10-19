from django.db import models

# Create your models here.


class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name

class Airports(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ident = models.CharField(max_length=100)

    def __str__(self):
        return self.name