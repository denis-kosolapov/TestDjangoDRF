from .models import FoodCategory, Food
from django_filters import rest_framework as filters

class CharFilterInFilter(filters.BaseInFilter, filters.BooleanFilter):
    pass

class FoodFilter(filters.FilterSet):
    food = CharFilterInFilter(field_name='food__is_publish', lookup_expr='in')
    is_publish = filters.BooleanFilter()

    class Meta:
        model = Food
        fields = ['is_publish']