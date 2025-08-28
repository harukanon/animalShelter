from django.db import models

# Base class for common animal attributes
class Sex(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    HERM = "H", "Hermaphrodite"


class IntakeMethod(models.TextChoices):
    AVAILABLE = "Y", "Available"
    ADOPTED = "N", "Adopted"
    UNKNOWN = "u", "Unknown"


class Status(models.TextChoices):
    INSPECTORS = "I", "Rescued by Inspectors"
    STRAY = "S", "Rescue from Stray"

    
class Species(models.Model):
    name = models.CharField(max_length=32)


class Breed(models.Model):
    name = models.CharField(max_length=32, blank=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=False)


class Animal(models.Model):
    name = models.CharField(max_length=32)
    dob = models.DateField()
    sex = models.CharField(max_length=1, choices=Sex.choices)
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    intake_method = models.CharField(
        max_length=1,
        choices=IntakeMethod.choices,
        verbose_name="Intake Method",
    )
    is_featured = models.BooleanField(default=False)
    image_url = models.ImageField(upload_to="animal_images/", default=None, null=False)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        verbose_name="Status",
        default="",
    )

    def clean(self):
        pass

