from dogs.models import Breed, Dog
from rest_framework import serializers


class DogSerializer(serializers.ModelSerializer):
    """
    Класс - сериализатор для модели собаки
    """

    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = (
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        )


class BreedSerializer(serializers.ModelSerializer):
    """
    Класс - сериализатор для модели породы
    """

    size = serializers.ChoiceField(choices=Breed.Size.choices)

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
        )
