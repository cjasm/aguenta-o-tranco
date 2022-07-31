from django.core.validators import MinValueValidator
from django.db import models

from meals.choices import MEALS_CATEGORIES, UNIT_CHOICES


class Nutrient(models.Model):
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=11, blank=True,
                            choices=UNIT_CHOICES, default='')
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Nutrient'
        verbose_name_plural = 'Nutrients'
        ordering = ['order']

    def __str__(self):
        return self.name


class NutritionFact(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE, related_name='nutrition')
    nutrient = models.ForeignKey('Nutrient', on_delete=models.CASCADE,
                                 related_name='nutrition_facts')
    value = models.FloatField()
    dv_percentage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name = 'Nutrition Fact'
        verbose_name_plural = 'Nutrition Facts'
        constraints = [
            models.UniqueConstraint(
                fields=['meal', 'nutrient'], name='nutrition_fact_unique_together_meal_nutrient')
        ]
        ordering = ['nutrient__order']

    def __str__(self):
        return '{nf.meal.title} - {nf.nutrient} - {nf.value}{nf.nutrient.unit}'.format(nf=self)


class Serving(models.Model):
    per_container = models.FloatField()
    size = models.FloatField()
    unit = models.CharField(max_length=11, blank=True, choices=UNIT_CHOICES, default='')

    def __str__(self):
        return 'Serv. Size: {serving.size} {serving.unit}, ' \
               'Serv. Per Container: {serving.per_container}'.format(serving=self)


class Meal(models.Model):
    category = models.CharField(
        choices=MEALS_CATEGORIES,
        default=MEALS_CATEGORIES.mains,
        max_length=25
    )
    sku = models.CharField(max_length=255, blank=False, unique=True)
    slug = models.SlugField(unique=True, db_index=True)

    title = models.TextField()
    description = models.TextField()
    serving_size = models.ForeignKey('meals.Serving', null=True, blank=True,
                                     related_name='meals', on_delete=models.CASCADE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return '{meal.title} - {meal.category}'.format(meal=self)
