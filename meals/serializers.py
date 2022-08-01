from rest_framework import serializers
from meals.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['sku', 'slug', 'title', 'description', 'category', 'start_date', 'end_date']
