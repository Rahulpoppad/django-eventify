from django.db import models
from django.contrib.auth import models as auth_models
import Event

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} - {self.event.name}"