from django.shortcuts import render
from rest_framework import viewsets
from .models import Team, Locatie
from .serializers import TeamSerializer, LocatieSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class LocatieViewSet(viewsets.ModelViewSet):
    queryset = Locatie.objects.all()
    serializer_class = LocatieSerializer
