import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='iexact') 
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains') 
    phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains') 

    class Meta:
        model = User
        fields = ['role', 'email', 'phone']
