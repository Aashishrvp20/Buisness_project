# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumericRangeFilter(field_name='price')     
    stock = django_filters.NumericRangeFilter(field_name='stock')    
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
 

    class Meta:
        model = Product
        fields = ['category', 'price', 'stock', 'name',]


