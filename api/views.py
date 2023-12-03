from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Product, Client, Order
from .serializers import ProductsSerlializer, CategorySerlializer, ClientSerializaer, CategoryProductSerializer, OrderSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerlializer


# class CategoryCreateView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerlializer(queryset)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerlializer


class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializaer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    lookup_url_kwarg = 'client_id'
    serializer_class = ClientSerializaer


class CategoryProductView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'category_id'
    serializer_class = CategoryProductSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
