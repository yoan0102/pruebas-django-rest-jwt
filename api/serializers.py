from rest_framework import serializers

from .models import Product, Category, Client, Order, OrderProduct


class ClientSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CategorySerlializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductsSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price',  'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url
        return representation


""" Serializer Realacionales """


class CategoryProductSerializer(serializers.ModelSerializer):
    Products = ProductsSerlializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'Products']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_product = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['code', 'client', 'order_product']

    def create(self, validated_data):
        order_products_list = validated_data.pop('order_product')
        order = Order.objects.create(**validated_data)
        for obj in order_products_list:
            OrderProduct.objects.create(order=order, **obj)

        return order
