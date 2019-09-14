from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    andrewID = models.CharField(max_length=20)
    college = models.CharField(max_length=10)
    
    def __str__(self):
        return self.andrewID


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=10)
    startTime = models.TimeField()
    endTime = models.TimeField()
    capacity = models.IntegerField()
    size = models.IntegerField()
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='the_leader')
    members = models.ManyToManyField(User, related_name='members')

    def __str__(self):
        return self.title

    def isFull(self):
        return self.size >= self.capacity

    def isEnded(self):
        return timezone.now() > self.endTime
