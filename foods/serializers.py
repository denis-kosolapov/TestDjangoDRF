from rest_framework import serializers
from .models import FoodCategory, Food

# отображает все объекты
class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class CategoryListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)
    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

# записывает данные в БД
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'


# отображает все объекты
class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'vin', 'user')

# записывает данные в БД
class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'