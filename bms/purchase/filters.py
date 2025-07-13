# filters.py
import django_filters
from .models import Purchase, Supplier, PurchaseReturn

class PurchaseFilter(django_filters.FilterSet):
    total = django_filters.NumericRangeFilter(field_name='total') 
    paid = django_filters.NumericRangeFilter(field_name='paid')   
    date = django_filters.DateFromToRangeFilter(field_name='date') 
    supplier = django_filters.CharFilter(field_name='supplier__name', lookup_expr='icontains')
    is_paid = django_filters.BooleanFilter()

    class Meta:
        model = Purchase
        fields = ['supplier', 'total', 'paid', 'is_paid', 'date']


class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'email']


class PurchaseReturnFilter(django_filters.FilterSet):
    refund_amount = django_filters.NumericRangeFilter(field_name='refund_amount')
    date = django_filters.DateFromToRangeFilter(field_name='date')
    purchase = django_filters.NumberFilter(field_name='purchase__id')

    class Meta:
        model = PurchaseReturn
        fields = ['purchase', 'refund_amount', 'date']
