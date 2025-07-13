from rest_framework import serializers
from .models import Course, Enrollment,Instructor,Student
from users.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import AllowAny

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_duration(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Duration description is too short.")
        return value

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['enrolled_at']
    
    def validate(self, attrs):
        student = attrs.get('student')
        course = attrs.get('course')

        if Enrollment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("This student is already enrolled in this course.")

        return attrs

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

    def validate(self, attrs):
        user = attrs.get('user')
        if user.role != 'instructor':
            raise serializers.ValidationError("User role must be 'instructor'.")
        return attrs

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        user = attrs.get('user')
        if user.role != 'student':
            raise serializers.ValidationError("User role must be 'student'.")
        return attrs
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'password', 'role')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        validated_data['role'] = 'student'  
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            role=validated_data['role'],
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.full_clean()
        user.save()
        return user
    

    
class InstructorRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(required=False)
    expertise = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Instructor
        fields = ['email', 'phone', 'password', 'bio', 'expertise', 'photo']

    def create(self, validated_data):
        email = validated_data.pop('email')
        phone = validated_data.pop('phone')
        password = validated_data.pop('password')

        # Create user with instructor role
        user = User.objects.create(
            email=email,
            phone=phone,
            username=email,
            role='instructor'
        )
        user.set_password(password)
        user.save()

        
        instructor = Instructor.objects.create(user=user, **validated_data)
        return instructor