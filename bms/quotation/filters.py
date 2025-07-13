# quotation/filters.py

import django_filters
from .models import Quotations

class QuotationFilter(django_filters.FilterSet):
    invoice_date = django_filters.DateFromToRangeFilter()  
    approved = django_filters.BooleanFilter()
    customer = django_filters.NumberFilter(field_name='customer__id')
    product_name = django_filters.CharFilter(lookup_expr='icontains')
    voucher_no = django_filters.NumberFilter()
    rate = django_filters.NumericRangeFilter()
    amount = django_filters.NumericRangeFilter()
    
    class Meta:
        model = Quotations
        fields = ['voucher_no', 'approved', 'invoice_date', 'customer', 'product_name', 'rate', 'amount']
