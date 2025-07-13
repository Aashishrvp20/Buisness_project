from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/enroll/', EnrollCourseView.as_view(), name='enroll-course'),
    path('my-courses/', MyCoursesView.as_view(), name='my-courses'),
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/register/', StudentRegisterView.as_view(), name='student-register'),
    path('instructors/register/', InstructorRegisterView.as_view(), name='instructor-register'),
]
