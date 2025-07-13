from rest_framework import serializers
from .models import *
from contact.serializers import CustomerSerializer

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['product', 'quantity', 'price']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    customer_detail = CustomerSerializer(source='customer', read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'customer_detail', 'date', 'total', 'discount', 'tax', 'paid', 'is_paid', 'items']

    def validate_items(self, value):
        if not value or len(value) == 0:
            raise serializers.ValidationError("At least one sale item is required.")
        return value
   
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sale.objects.create(**validated_data)
        for item in items_data:
            SaleItem.objects.create(sale=sale, **item)
        return sale
    
    
class SaleReturnItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleReturnItem
        fields = ['sale_item', 'quantity']

class SaleReturnSerializer(serializers.ModelSerializer):
    items = SaleReturnItemSerializer(many=True)

    class Meta:
        model = SaleReturn
        fields = ['id', 'sale', 'date', 'refund_amount', 'items']

    def validate_refund_amount(self,value):
        if value <=0:
            raise serializers.ValidationError('refun amount must be more than 0')
        
    def validate_sale(self,value):
        if value is None:
            raise serializers.ValidationError('Sales item was not found')    

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale_return = SaleReturn.objects.create(**validated_data)
        for item_data in items_data:
            SaleReturnItem.objects.create(sale_return=sale_return, **item_data)
        return sale_return

class SalesAnalyticsSerializer(serializers.Serializer):
    sales_7days = serializers.DecimalField(max_digits=12, decimal_places=2)
    sales_30days = serializers.DecimalField(max_digits=12, decimal_places=2)
    returns_7days = serializers.DecimalField(max_digits=12, decimal_places=2)
    returns_30days = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_last_7days = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_last_30days = serializers.DecimalField(max_digits=12, decimal_places=2)