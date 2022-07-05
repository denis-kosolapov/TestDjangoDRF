from rest_framework import generics
from .serializers import CategoryDetailSerializer, CategoryListSerializer, FoodDetailSerializer, FoodListSerializer
from .models import FoodCategory, Food


# записывает данные в БД
class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer

# отображает все объекты
class CategorysListView(generics.ListAPIView):

    serializer_class = CategoryListSerializer
    queryset = FoodCategory.objects.all()

# смотр конкретной записи и ее редактирование
class CategoryDeatilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = FoodCategory.objects.all()



# записывает данные в БД
class FoodCreateView(generics.CreateAPIView):
    serializer_class = FoodDetailSerializer

# отображает все объекты
class FoodsListView(generics.ListAPIView):
    serializer_class = FoodListSerializer
    queryset = Food.objects.all()

# смотр конкретной записи и ее редактирование
class FoodDeatilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodDetailSerializer
    queryset = Food.objects.all()