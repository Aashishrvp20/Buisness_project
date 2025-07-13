from rest_framework import serializers
from .models import ExpenseCategory, IncomeCategory, Expense, Income

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def validate_amount(self,value):
        if value<=0:
            raise serializers.ValidationError('Amount must be more than 0')
        return value
    
    def validate_category(self,value):
        if value is None:
            raise serializers.ValidationError("Expense catergory is required")
        return value


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

    def validate_amount(self,value):
        if value<=0:
            raise serializers.ValidationError('Amount must be more than 0')
        return value
    
    def validate_category(self,value):
        if value is None:
            raise serializers.ValidationError("Income catergory is required")
        return value
