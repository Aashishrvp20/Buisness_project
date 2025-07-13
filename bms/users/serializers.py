from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Permission
from .role_permissions import get_role_permissions

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model=User
        fields=('id','email','phone','password','role',)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        role=validated_data.get('role', 'staff'),
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            role=role
            
            username=validated_data['email'] 
        )
        user.set_password(validated_data['password'])
        user.full_clean()
        user.save()
        role_permissions = get_role_permissions()
        permissions = role_permissions.get(role)
        if permissions:
            user.user_permissions.set(permissions)
        
        return user
    
