from rest_framework import serializers
from .models import *

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity', 'price']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value    

class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True)
    invoice_file = serializers.FileField(required=False)

    class Meta:
        model = Purchase
        fields = ['id', 'supplier', 'date', 'total', 'paid', 'is_paid', 'items','invoice_file']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase = Purchase.objects.create(**validated_data)
        for item in items_data:
            PurchaseItem.objects.create(purchase=purchase, **item)
        return purchase
    
class PurchaseReturnItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseReturnItem
        fields = ['purchase_item', 'quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Return quantity must be greater than 0.")
        return value
    
    def validate_purchase_item(self,value):
        if value in None:
            raise serializers.ValidationError("purchased item must be specified")
        return value

class PurchaseReturnSerializer(serializers.ModelSerializer):
    items = PurchaseReturnItemSerializer(many=True)

    class Meta:
        model = PurchaseReturn
        fields = ['id', 'purchase', 'date', 'refund_amount', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase_return = PurchaseReturn.objects.create(**validated_data)
        for item_data in items_data:
            PurchaseReturnItem.objects.create(purchase_return=purchase_return, **item_data)
        return purchase_return