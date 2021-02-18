from django.db import models
from django.utils import timezone
import factory

# Create your models here.


class Entry(models.Model):
    entry_text = models.CharField(max_length=50, required = True, unique = True)


class Puzzle(models.Model):
    title = models.CharField(max_length=255, blank = True)
    date = models.DateTimeField(default=timezone.now, required = True)
    byline = models.CharField(max_length=255, required = True)
    publisher = models.CharField(max_length=255, required = True)


class Clue(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    clue_text = models.CharField(max_length=512, required = True)
    theme = models.BooleanField(default=False)


