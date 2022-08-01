from rest_framework import generics, permissions
from meals.models import Meal
from meals import serializers


class MealListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows meals to be viewed or edited.
    """
    queryset = Meal.objects.all()
    serializer_class = serializers.MealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

