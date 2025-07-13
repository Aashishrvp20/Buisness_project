from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class ReviewListView(ListCreateAPIView):
    queryset=MyReview.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]

# Create your views here.
