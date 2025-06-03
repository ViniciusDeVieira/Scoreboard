from django.shortcuts import render
from .models import Team, Locatie
from .serializers import TeamSerializer, LocatieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Teamlist(APIView):
    def get(self,request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        return Response(serializer.data)

class Locatielist(APIView):
    def get(self, request):
        locaties = Locatie.objects.all()
        serializer = LocatieSerializer(locaties, many=True, context={'request': request})
        return Response(serializer.data)
    
class Teamslistadmin(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeamSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class Locatielistadmin(APIView):
    def get(self, request):
        locaties = Locatie.objects.all()
        serializer = LocatieSerializer(locaties, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LocatieSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TeamDetailadmin(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return None

    def get(self, request, pk):
        team = self.get_object(pk)
        if team is None:
            return Response(status=404)
        serializer = TeamSerializer(team, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        team = self.get_object(pk)
        if team is None:
            return Response(status=404)
        serializer = TeamSerializer(team, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        team = self.get_object(pk)
        if team is None:
            return Response(status=404)
        team.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        team = self.get_object(pk)
        if team is None:
            return Response(status=404)
        serializer = TeamSerializer(team, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class LocatieDetailadmin(APIView):
    def get_object(self, pk):
        try:
            return Locatie.objects.get(pk=pk)
        except Locatie.DoesNotExist:
            return None

    def get(self, request, pk):
        locatie = self.get_object(pk)
        if locatie is None:
            return Response(status=404)
        serializer = LocatieSerializer(locatie, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        locatie = self.get_object(pk)
        if locatie is None:
            return Response(status=404)
        serializer = LocatieSerializer(locatie, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        locatie = self.get_object(pk)
        if locatie is None:
            return Response(status=404)
        locatie.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        locatie = self.get_object(pk)
        if locatie is None:
            return Response(status=404)
        serializer = LocatieSerializer(locatie, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    


from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TokenRefreshView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(data)
