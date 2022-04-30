from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.value)
