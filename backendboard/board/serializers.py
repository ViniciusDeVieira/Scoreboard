from rest_framework import serializers

from .models import Team, Locatie  # Import your models here

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'  # You can specify the fields you want to include

class LocatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locatie
        fields = '__all__'  # You can specify the fields you want to include