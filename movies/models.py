from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies'
        )
    release_data = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
