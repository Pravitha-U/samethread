from django.db import models

# Create your models here.
from django.db import models


class SampleModel(models.Model):
    name = models.CharField(max_length=100)

