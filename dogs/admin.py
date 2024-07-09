from django.contrib import admin
from dogs.models import Breed, Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "breed", "gender", "color")
    list_display_links = ("id", "name")
    fields = [
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    ]
    list_per_page = 5
    search_fields = ["breed_name"]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "size")
    list_display_links = ("id", "name")
    fields = [
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    ]
    list_per_page = 5
    search_fields = ["name"]
