from django.db import models
from django.core import validators

# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=False)
    quantity = models.IntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)]
    )
