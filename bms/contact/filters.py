import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    date_created = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'date_created']
