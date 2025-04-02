from django.db import models

# Create your models here.
class animalDatabase(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.TextField(max_length=32)
    dateOfBirth = models.DateField()
    gender = models.BooleanField()
    breed = models.TextField(max_length=32)
    intakeMethod = models.TextField(max_length=32)
    notes = models.TextField(max_length=256)
    status = models.TextField(max_length=32)
