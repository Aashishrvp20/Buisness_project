from .models import *
from rest_framework import serializers

class QuotationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quotations
        fields="__all__" 
        read_only_fields=['amount','invoice_date']


        
    def validate_rate(self, value):
        if value <= 0:
            raise serializers.ValidationError("Rate must be greater than 0.")
        return value

    def validate_discount(self, value):
        if value < 0:
            raise serializers.ValidationError("Discount cannot be negative.")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value

    def validate_voucher_no(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Voucher number must be positive.")
        return value

    def validate(self, data):
        rate = data.get('rate')
        quantity = data.get('quantity')
        discount = data.get('discount')

        if rate is not None and quantity is not None and discount is not None:
            total = rate * quantity
            if discount > total:
                raise serializers.ValidationError("Discount cannot be greater than the total amount (rate x quantity).")

        return data