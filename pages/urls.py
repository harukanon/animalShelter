from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.homepage, name="homepage"),
    path("list/", views.pet_list, name='pet_list'),
    path('<str:pet_type>/<str:name>/', views.pet_detail, name='pet_detail'),
]