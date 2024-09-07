from django.db import models

# Create your models here.

class Play(models.Model):
    title = models.CharField(max_length=255)
    annotations = models.TextField()

class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True)


class Show(models.Model):
    starts_at = models.DateTimeField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor.)

