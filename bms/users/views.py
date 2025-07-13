from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView
from .serializers import RegisterSerializer,UserPermissionUpdateSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from .permissions import Admin




class RegisterView(CreateAPIView):
    data= User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [Admin]


class CookieTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            access_token = data.get('access')
            refresh_token = data.get('refresh')

            
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                samesite='Lax',
                secure=False,  
                max_age=60 * 60  
            )
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                samesite='Lax',
                secure=False,
                max_age=60 * 60 * 24 * 7 
            )

        return response
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response

class UserPermissionUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPermissionUpdateSerializer
    permission_classes = [Admin]
    lookup_field = 'id'