from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Dog(models.Model):
    """
    Модель собаки
    """

    name = models.CharField(
        max_length=255, null=False, unique=True, verbose_name="Кличка"
    )
    age = models.IntegerField(null=False, verbose_name="Возраст")
    breed = models.ForeignKey(
        "Breed", on_delete=models.CASCADE, related_name="dogs", verbose_name="Порода"
    )
    gender = models.CharField(max_length=255, null=False, verbose_name="Пол")
    color = models.CharField(max_length=255, null=False, verbose_name="Окраска")
    favorite_food = models.CharField(
        max_length=255, null=False, verbose_name="Любимая еда"
    )
    favorite_toy = models.CharField(
        max_length=255, null=False, verbose_name="Любимая игрушка"
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"


class Breed(models.Model):
    """
    Модель породы
    """

    class Size(models.TextChoices):
        TINY = "TN", "Tiny"
        SMALL = "SM", "Small"
        MEDIUM = "MD", "Medium"
        LARGE = "LG", "Large"

    name = models.CharField(max_length=255, null=False, verbose_name="Название")
    size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.TINY, verbose_name="Размер"
    )
    friendliness = models.IntegerField(
        null=False,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Удобство",
    )
    trainability = models.IntegerField(
        null=False,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Обучаемость",
    )
    shedding_amount = models.IntegerField(
        null=False,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Количество выпадения шерсти",
    )
    exercise_needs = models.IntegerField(
        null=False,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Потребности в физических упражнениях",
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
