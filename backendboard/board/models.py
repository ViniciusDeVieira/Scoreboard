from django.db import models

class Locatie(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='locatie_fotos/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Team(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='team_fotos/', blank=True, null=True)
    locatie = models.ForeignKey(Locatie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.locatie.name})' 