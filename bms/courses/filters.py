import django_filters
from .models import Course,Instructor, Student

class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    instructor = django_filters.NumberFilter(field_name='instructor__id')  
    price = django_filters.RangeFilter()
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Course
        fields = ['title', 'instructor', 'price', 'created_at']
class InstructorFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='user__email', lookup_expr='icontains')
    expertise = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Instructor
        fields = ['username', 'email', 'expertise']


class StudentFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='user__email', lookup_expr='icontains')
    enrolled_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Student
        fields = ['username', 'email', 'enrolled_date']



