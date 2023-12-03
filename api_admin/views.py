from rest_framework import viewsets
from api.models import Category, Product
from api.serializers import CategorySerlializer, ProductsSerlializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerlializer
