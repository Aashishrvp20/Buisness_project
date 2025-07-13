import django_filters
from .models import Expense, Income

class ExpenseFilter(django_filters.FilterSet):
    amount = django_filters.NumericRangeFilter(field_name="amount")  
    date = django_filters.DateFilter(field_name="date")
    date_range = django_filters.DateFromToRangeFilter(field_name="date")
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='icontains')

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date', 'date_range']


class IncomeFilter(django_filters.FilterSet):
    amount = django_filters.NumericRangeFilter(field_name="amount")
    date = django_filters.DateFilter(field_name="date")
    date_range = django_filters.DateFromToRangeFilter(field_name="date")
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='icontains')

    class Meta:
        model = Income
        fields = ['category', 'amount', 'date', 'date_range']
