from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Cat, Dog, Rabbit


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    cats = Cat.objects.all()
    dogs = Dog.objects.all()
    rabbits = Rabbit.objects.all()

    featured_cat = Cat.objects.filter(featured=True).first()
    featured_dog = Dog.objects.filter(featured=True).first()
    featured_rabbit = Rabbit.objects.filter(featured=True).first()

    return render(request, 'pages/homepage.html', {
        'cats': cats,
        'dogs': dogs,
        'rabbits': rabbits,
        'featured_cat': featured_cat,
        'featured_dog': featured_dog,
        'featured_rabbit': featured_rabbit,
    })

def pet_detail(request, pet_type, name):
    model_map = {
        'cat': Cat,
        'dog': Dog,
        'rabbit': Rabbit,
    }

    model = model_map.get(pet_type.lower())
    if not model:
        return render(request, '404.html', status=404)

    # Case-insensitive name match
    pet = get_object_or_404(model, name__iexact=name)
    return render(request, 'pages/pet_detail.html', {'pet': pet})

from .models import Cat, Dog, Rabbit
from itertools import chain

def pet_list(request):
    cats = Cat.objects.all()
    dogs = Dog.objects.all()
    rabbits = Rabbit.objects.all()

    all_pets = list(chain(cats, dogs, rabbits))

    return render(request, 'pages/pet_list.html', {'pets': all_pets})
