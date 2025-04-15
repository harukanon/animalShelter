from django.db import models

# Create your models here.
class animals(models.Model):
    id = models.SmallAutoField(primary_key=True)
    firstName = models.TextField(max_length=32)
    lastName = models.TextField(max_length=32)
    dateOfBirth = models.DateField()
    gender = models.BooleanField()
    breed = models.TextField(max_length=32)
    intakeMethod = models.TextField(max_length=32)
    notes = models.TextField(max_length=256)
    status = models.TextField(max_length=32)
    def __str__(self):
        return self.name
