from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse
from django.conf import settings
import socket
import logging

logger = logging.getLogger(__name__)

def api_root(request):
    host = request.get_host()
    server_name = socket.gethostname()
    logger.debug(f"Request Host: {host}, Server Name: {server_name}")
    base_url = "https://cautious-enigma-vpjpx56x4v3prp9-8000.app.github.dev" if "cautious-enigma" in host else "http://localhost:8000"
    return JsonResponse({
        "host": host,
        "server_name": server_name,
        "users": f"{base_url}/users/",
        "teams": f"{base_url}/teams/",
        "activities": f"{base_url}/activities/",
        "leaderboards": f"{base_url}/leaderboards/",
        "workouts": f"{base_url}/workouts/"
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer