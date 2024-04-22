from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    thumbnail = models.URLField()

    def __str__(self):
        return self.name