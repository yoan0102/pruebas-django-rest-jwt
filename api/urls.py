from django.urls import path
from .views import CategoryListView, ProductListView, ClientListView, ClientDetailView, CategoryProductView, OrderCreateView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:category_id>/products', CategoryProductView.as_view()),
    path('products/', ProductListView.as_view()),
    path('clients/', ClientListView.as_view()),
    path('clients/<int:client_id>', ClientDetailView.as_view()),
    path('order/', OrderCreateView.as_view()),
]
