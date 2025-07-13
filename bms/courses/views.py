from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
from .models import Course, Enrollment,Instructor,Student
from .serializers import *
from users.permissions import Manager,Staff
import tablib
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter,InstructorFilter, StudentFilter

class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [Staff]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [Manager]


class EnrollCourseView(CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [Staff]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyCoursesView(ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [Manager]

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)
    
class InstructorListCreateView(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InstructorFilter
    permission_classes = [Manager]  

class StudentRegisterView(CreateAPIView):
    serializer_class = RegistersSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save(role='student')

       
        Student.objects.create(user=user, photo=request.FILES.get('photo'))

        return Response({
            "message": "Student registered successfully",
            "user": RegisterSerializer(user).data
        }, status=status.HTTP_201_CREATED)

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter
    permission_classes = [Staff ] 

class InstructorRegisterView(CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorRegisterSerializer
    permission_classes = [Manager]



def Courses_csv(request): # sale
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['title', 'description', 'instructor', 'duration ','price','created_at']
    
    # Add your data
    for obj in Course.objects.all():
        dataset.append([obj.title, obj.description, obj.instructor, obj.duration,obj.price,obj.created_at])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return response    
def Enrollment_csv(request): # Enrollemnt
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['user', 'course', 'enrolled_at']
    
    # Add your data
    for obj in Enrollment.objects.all():
        dataset.append([obj.user, obj.course, obj.enrolled_at])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return response   
