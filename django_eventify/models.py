from django.db import models
from django.contrib.auth import models as auth_models

class Event(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    thumbnail = models.URLField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} - {self.event.name}"