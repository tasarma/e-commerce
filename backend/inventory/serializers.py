from rest_framework import serializers
from .models import Order, OrderItem, Product, ProductOrderingInformations, ProductSpesifications, ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSpesificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpesifications
        fields = "__all__"


class ProductOrderingInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrderingInformations
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = "__all__"

class ShippingAddresserializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"