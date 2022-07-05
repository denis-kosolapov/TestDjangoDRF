from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'foods'
urlpatterns = [
    path('food_category/create/', CategoryCreateView.as_view()),
    path('', CategorysListView.as_view()),
    path('food_category/detail/<int:pk>/', CategoryDeatilView.as_view()),

    path('food/create/', FoodCreateView.as_view()),
    path('foody/detail/<int:pk>/', FoodDeatilView.as_view()),
]
