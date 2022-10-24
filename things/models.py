from django.db.models import Model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Thing(Model):
    name = models.CharField(
    max_length = 30,
    unique = True
    )
    description = models.CharField(
    max_length = 120,
    blank = True
    )
    quantity = models.IntegerField(
    default = 0,
    validators = [
    MinValueValidator(0),
    MaxValueValidator(100),
    ]
    )
