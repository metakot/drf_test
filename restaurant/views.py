from rest_framework.generics import ListAPIView

from .models import FoodCategory
from .serializers import FoodListSerializer


class CategoriesWithInnerFoodsListView(ListAPIView):
    serializer_class = FoodListSerializer
    pagination_class = None  # ensure format needed in task
    # ensure filter and order needed in task
    queryset = FoodCategory.objects.filter(food__is_publish=True).distinct().order_by('order_id')
