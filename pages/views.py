from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Animal


def index(request):
    '''
    returns all pets
    '''
    Animal.objects.all()
    return render(request, "pages/index.html")

def pet_detail(request, pet_type, name):
    '''
    gets all information regarding a given pet
    '''
    pet = get_object_or_404(Animal.objects.filter(breed__name__iexact=breed), name__iexact=name)
    return render(request, "pages/pet_detail.html")

def pet_list(request):
    # list all pets
    return render(request, "pages/pet_list.html")