from rest_framework import serializers
from .models import Customer
from purchase.models import Supplier

class CustomerSerializer(serializers.ModelSerializer):
    def validate_opening_blnc(self, value):
        if value < 0:
            raise serializers.ValidationError("Opening balance cannot be negative.")
        return value
    
    class Meta:
        model = Customer
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
class CustomerLedgerSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    total_sales = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_paid = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_returns = serializers.DecimalField(max_digits=12, decimal_places=2)
    balance_due = serializers.DecimalField(max_digits=12, decimal_places=2)


class SupplierLedgerSerializer(serializers.Serializer):
    supplier_id = serializers.IntegerField()
    total_purchases = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_paid = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_returns = serializers.DecimalField(max_digits=12, decimal_places=2)
    balance_due = serializers.DecimalField(max_digits=12, decimal_places=2)
