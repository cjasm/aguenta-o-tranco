from django.urls import path
from meals import views

urlpatterns = [
    path('', views.MealListCreateAPIView.as_view(), name='meals-list')
]
