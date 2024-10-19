from rest_framework import serializers
from .models import Order
from products.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'product', 'quantity']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']

        if product.stock_quantity < quantity:
            raise serializers.ValidationError("Insufficient stock available.")
        
        return data

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        product.stock_quantity -= quantity
        product.save()
        return super().create(validated_data)
