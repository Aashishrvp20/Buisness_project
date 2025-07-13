from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .serializers import ProductSerializer, CategorySerializer, StockEntrySerializer
from users.permissions import Manager,Staff
from .models import *
import tablib
from django.http import HttpResponse
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [Staff]

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [Manager]    

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [Staff]

class StockEntryCreateView(CreateAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = StockEntrySerializer
    permission_classes = [Staff]
    
def product_csv(request): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['name', 'category', 'unit', 'price','stock','low_stock']
    
    # Add your data
    for obj in Product.objects.all():
        dataset.append([obj.name, obj.category, obj.unit, obj.price,obj.stock,obj.low_stock])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    return response

def product_id_csv(request,id): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['name', 'category', 'unit', 'price','stock','low_stock']
    
    # Add your data
    for obj in Product.objects.filter(id=id):
        dataset.append([obj.name, obj.category, obj.unit, obj.price,obj.stock,obj.low_stock])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product_by_id.csv"'
    return response