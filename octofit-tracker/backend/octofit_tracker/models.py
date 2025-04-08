from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    team = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    members = models.JSONField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

class Workout(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name