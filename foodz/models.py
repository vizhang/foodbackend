from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    imageURI = models.TextField(validators=[URLValidator()])
    isMade = models.IntegerField

class User(models.Model):
    username = models.CharField(max_length=240)

class History(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
    comment = models.TextField()
    rating = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
