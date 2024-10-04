from rest_framework import serializers
from .models import Purchase
from products.models import Product

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['purchase_id', 'product', 'quantity']

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
