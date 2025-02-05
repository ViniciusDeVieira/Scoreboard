from django.db import models

class Locatie(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

class Team(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    locatie = models.ForeignKey('Locatie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.locatie.name})'