from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *


class ReviewListView(ListCreateAPIView):
    queryset=MyReview.objects.all()
    serializer_class=ReviewSerializer
    

# Create your views here.
