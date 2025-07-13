# sales/filters.py

import django_filters
from .models import Sale, SaleReturn

class SaleFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter() 
    is_paid = django_filters.BooleanFilter()
    customer = django_filters.NumberFilter(field_name='customer__id')
    total = django_filters.RangeFilter()
    created_by = django_filters.NumberFilter(field_name='created_by__id')

    class Meta:
        model = Sale
        fields = ['customer', 'is_paid', 'date', 'total', 'created_by']

class SaleReturnFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter()
    sale = django_filters.NumberFilter(field_name='sale__id')
    refund_amount = django_filters.RangeFilter()

    class Meta:
        model = SaleReturn
        fields = ['sale', 'date', 'refund_amount']
