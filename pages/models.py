from django.db import models

# Base class for common animal attributes
class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()  # Use PositiveIntegerField for age
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    featured = models.BooleanField(default=False) 
    CAT = "cat"
    DOG = "dog"
    RABBIT = "rabbit"
    FOX = "fox"
    PET_TYPES = {CAT: "cat", DOG: "dog", RABBIT: "rabbit", FOX:"fox"}
    pet_type = models.CharField(max_length=10, choices= PET_TYPES)
    image = models.ImageField(upload_to='animal_images/', null=True, blank=True)

    class Meta:
        abstract = True  # This class is just for inheritance, no table will be created

class Cat(Animal):
    breed = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.type = "Cat"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - Cat'


class Dog(Animal):
    breed = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.type = "Dog"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - Dog'


class Rabbit(Animal):
    breed = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.type = "Rabbit"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - Rabbit'

class Fox(Animal):
    breed = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.type = "Fox"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - Fox'


